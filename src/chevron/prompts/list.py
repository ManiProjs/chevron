

from __future__ import annotations

from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl

from .base import BasePrompt


class ListPrompt(BasePrompt):
    def __init__(self, message: str, choices: list[str], *, theme=None):
        super().__init__(message, theme=theme)
        if not choices:
            raise ValueError("choices cannot be empty")
        self.choices = choices
        self.index = 0
        self._bindings = KeyBindings()
        self._result = None

        @self._bindings.add("up")
        @self._bindings.add("k")
        def _(event):
            self.move_up()

        @self._bindings.add("down")
        @self._bindings.add("j")
        def _(event):
            self.move_down()

        @self._bindings.add("c-c")
        def _(event):
            raise KeyboardInterrupt

    def move_up(self):
        self.index = (self.index - 1) % len(self.choices)

    def move_down(self):
        self.index = (self.index + 1) % len(self.choices)

    def render_header(self):
        return [
            (self.theme.pointer_style, f"{self.theme.pointer} "),
            (self.theme.message_style, self.message),
            ("", "\n\n"),
        ]

    def render_choice(self, index: int, choice: str):
        current = index == self.index
        style = self.theme.selected_style if current else ""
        prefix = f"{self.theme.pointer} " if current else "  "
        return [(style, f"{prefix}{choice}\n")]

    def render_footer(self):
        return [
            (self.theme.footer_style, "\n↑↓ Navigate • Enter Confirm")
        ]

    def render(self):
        lines = []
        lines.extend(self.render_header())

        for i, choice in enumerate(self.choices):
            lines.extend(self.render_choice(i, choice))

        lines.extend(self.render_footer())
        return lines

    def run(self):
        app = Application(
            layout=Layout(Window(FormattedTextControl(lambda: self.render()))),
            key_bindings=self._bindings,
            full_screen=False,
        )
        app.run()
        return self._result