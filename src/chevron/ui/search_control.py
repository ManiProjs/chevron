from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence, Optional, Callable

from prompt_toolkit.application import Application
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import TextArea


@dataclass
class SearchItem:
    value: Any
    label: str
    description: str | None = None


class SearchControl:
    def __init__(
        self,
        message: str,
        choices: Sequence[str | SearchItem],
        theme,
        *,
        display: Optional[Callable[[Any], str]] = None,
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

        self.display = display
        self.result: Any = None

    def run(self) -> Any:
        control = _SearchPrompt(
            choices=self.choices,
            theme=self.theme,
            display=self.display,
        )

        style = Style.from_dict(
            {
                "message": self.theme.message_style,
                "pointer": self.theme.pointer_style,
                "selected": self.theme.pointer_style,
                "description": "ansibrightblack",
                "query": "",
            }
        )

        kb = KeyBindings()

        @kb.add("c-c")
        @kb.add("escape")
        def cancel(event):
            event.app.exit(result=None)

        @kb.add("up")
        def up(event):
            control.move_selection(-1)
            event.app.invalidate()

        @kb.add("down")
        def down(event):
            control.move_selection(1)
            event.app.invalidate()

        @kb.add("enter")
        def accept(event):
            event.app.exit(
                result=control.current_selection()
            )

        layout = Layout(
            HSplit(
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
                    control.input,
                    Window(
                        content=control.results_control,
                    ),
                ]
            )
        )

        app = Application(
            layout=layout,
            key_bindings=kb,
            style=style,
            mouse_support=False,
            full_screen=False,
        )

        try:
            self.result = app.run()
        except KeyboardInterrupt:
            self.result = None

        return self.result


class _SearchPrompt:
    def __init__(
        self,
        choices: list[SearchItem],
        theme,
        display: Optional[Callable[[Any], str]],
    ):
        self.choices = choices
        self.theme = theme
        self.display = display

        self.matches = choices.copy()

        self.selected = 0
        self.scroll_offset = 0

        self.visible_items = 6

        self.input = TextArea(
            text="",
            multiline=False,
            prompt="> ",
            height=1,
            style="class:query",
            focusable=True,
        )

        self.input.buffer.on_text_changed += (
            self._on_query_changed
        )

        self.results_control = FormattedTextControl(
            self._get_results
        )

    def _label(self, item: SearchItem) -> str:
        if self.display:
            return self.display(item.value)

        return item.label

    def _fuzzy_match(
        self,
        query: str,
        text: str,
    ) -> bool:
        if not query:
            return True

        query = query.lower()
        text = text.lower()

        index = 0

        for char in query:
            index = text.find(char, index)

            if index == -1:
                return False

            index += 1

        return True

    def _on_query_changed(self, _):
        query = self.input.text

        self.matches = [
            item
            for item in self.choices
            if self._fuzzy_match(
                query,
                self._label(item),
            )
        ]

        self.selected = 0
        self.scroll_offset = 0

    def move_selection(self, amount: int):
        if not self.matches:
            return

        self.selected = (
            self.selected + amount
        ) % len(self.matches)

        self._ensure_visible()

    def _ensure_visible(self):
        if self.selected < self.scroll_offset:
            self.scroll_offset = self.selected

        elif (
            self.selected
            >= self.scroll_offset + self.visible_items
        ):
            self.scroll_offset = (
                self.selected
                - self.visible_items
                + 1
            )

    def current_selection(self):
        if not self.matches:
            return None

        return self.matches[self.selected].value

    def _get_results(self):
        if not self.matches:
            return [
                (
                    "class:description",
                    "  No results",
                )
            ]

        self._ensure_visible()

        visible = self.matches[
            self.scroll_offset:
            self.scroll_offset + self.visible_items
        ]

        lines = []

        for index, item in enumerate(
            visible,
            start=self.scroll_offset,
        ):
            selected = index == self.selected

            prefix = (
                self.theme.pointer
                if selected
                else " "
            )

            style = (
                "class:selected"
                if selected
                else ""
            )

            lines.append(
                (
                    style,
                    f"{prefix} {self._label(item)}\n",
                )
            )

            if item.description:
                lines.append(
                    (
                        "class:description",
                        f"    {item.description}\n",
                    )
                )

        lines.append(
            (
                "class:description",
                f"\n  {self.selected + 1}/{len(self.matches)}",
            )
        )

        return lines
