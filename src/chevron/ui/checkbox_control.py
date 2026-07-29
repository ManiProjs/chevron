from __future__ import annotations

from typing import Sequence

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl


class CheckboxControl:
    def __init__(
        self,
        message: str,
        choices: Sequence[str],
        default: Sequence[str],
        theme,
    ):
        self.message = message
        self.choices = list(choices)
        self.theme = theme

        self.selected = set(default)
        self.selection_order = list(default)
        self.index = 0

        self.control = FormattedTextControl(self.render)

        self.window = Window(self.control)

        self.key_bindings = self.create_keybindings()

    def render(self):
        lines = []

        lines.append(
            (
                self.theme.message_style,
                f"{self.theme.pointer} {self.message}\n",
            )
        )

        for i, choice in enumerate(self.choices):
            checked = choice in self.selected

            icon = self.theme.checked_icon if checked else self.theme.unchecked_icon

            prefix = self.theme.pointer if i == self.index else " "

            style = self.theme.selected_style if i == self.index else ""

            lines.append(
                (
                    style,
                    f"{prefix} {icon} {choice}\n",
                )
            )

        lines.append(
            (
                self.theme.footer_style,
                f"\n{len(self.selected)} selected"
                " • ↑↓ Move • Space Toggle • Enter Confirm",
            )
        )

        return lines

    def create_keybindings(self):
        kb = KeyBindings()

        @kb.add("up")
        def _(event):
            self.index = (self.index - 1) % len(self.choices)

            event.app.invalidate()

        @kb.add("down")
        def _(event):
            self.index = (self.index + 1) % len(self.choices)

            event.app.invalidate()

        @kb.add("space")
        def _(event):
            choice = self.choices[self.index]

            if choice in self.selected:
                self.selected.remove(choice)
                self.selection_order.remove(choice)
            else:
                self.selected.add(choice)
                self.selection_order.append(choice)

            event.app.invalidate()

        @kb.add("enter")
        def _(event):
            event.app.exit(result=self.selection_order.copy())

        @kb.add("c-c")
        def _(event):
            event.app.exit(result=None)

        return kb
