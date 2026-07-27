from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence, Optional, Any

from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import TextArea

from chevron.ui.control import PromptControl


@dataclass(slots=True)
class SearchItem:
    value: Any
    label: str
    description: Optional[str] = None


class SearchControl(PromptControl):
    def __init__(
        self,
        message: str,
        choices: Sequence[str | SearchItem],
        theme,
    ) -> None:
        self.message = message
        self.theme = theme

        self.choices = [
            item
            if isinstance(item, SearchItem)
            else SearchItem(
                value=item,
                label=str(item),
            )
            for item in choices
        ]

        self.matches = self.choices.copy()

        self.selected = 0
        self.scroll_offset = 0
        self.visible_items = 6

        self.input = TextArea(
            text="",
            multiline=False,
            prompt="> ",
            height=1,
            style="class:query",
        )

        self.input.buffer.on_text_changed += self._on_query_changed

        self.results_control = FormattedTextControl(self._render_results)

        self._window = HSplit(
            [
                Window(
                    content=FormattedTextControl(
                        FormattedText(
                            [
                                (
                                    "class:message",
                                    f"{self.theme.pointer} {self.message}",
                                )
                            ]
                        )
                    ),
                    height=1,
                ),
                self.input,
                Window(
                    content=self.results_control,
                ),
            ]
        )

        self._key_bindings = self._create_key_bindings()

    @property
    def window(self):
        return self._window

    @property
    def key_bindings(self):
        return self._key_bindings

    def _fuzzy_match(
        self,
        query: str,
        text: str,
    ) -> bool:
        if not query:
            return True

        query = query.lower()
        text = text.lower()

        position = 0

        for char in query:
            position = text.find(char, position)

            if position == -1:
                return False

            position += 1

        return True

    def _on_query_changed(self, _):
        query = self.input.text

        self.matches = [
            item
            for item in self.choices
            if self._fuzzy_match(
                query,
                item.label,
            )
        ]

        self.selected = 0
        self.scroll_offset = 0

    def _move_selection(self, amount: int):
        if not self.matches:
            return

        self.selected = (self.selected + amount) % len(self.matches)

        self._ensure_visible()

    def _ensure_visible(self):
        if self.selected < self.scroll_offset:
            self.scroll_offset = self.selected

        elif self.selected >= self.scroll_offset + self.visible_items:
            self.scroll_offset = self.selected - self.visible_items + 1

    def current_selection(self):
        if not self.matches:
            return None

        return self.matches[self.selected].value

    def _render_results(self):
        if not self.matches:
            return [
                (
                    "class:error",
                    "  No results",
                )
            ]

        self._ensure_visible()

        lines = []

        visible = self.matches[
            self.scroll_offset : self.scroll_offset + self.visible_items
        ]

        for index, item in enumerate(
            visible,
            start=self.scroll_offset,
        ):
            selected = index == self.selected

            prefix = self.theme.pointer if selected else " "

            style = "class:selected" if selected else ""

            lines.append(
                (
                    style,
                    f"{prefix} {item.label}\n",
                )
            )

            if item.description:
                lines.append(
                    (
                        "class:description",
                        f"    {item.description}\n",
                    )
                )

        if len(self.matches) > self.visible_items:
            lines.append(
                (
                    "class:description",
                    f"\n  {self.selected + 1}/{len(self.matches)}",
                )
            )

        return lines

    def _create_key_bindings(self):
        kb = KeyBindings()

        @kb.add("up")
        def _(event):
            self._move_selection(-1)
            event.app.invalidate()

        @kb.add("down")
        def _(event):
            self._move_selection(1)
            event.app.invalidate()

        @kb.add("enter")
        def _(event):
            event.app.exit(result=self.current_selection())

        @kb.add("escape")
        @kb.add("c-c")
        def _(event):
            event.app.exit(result=None)

        return kb
