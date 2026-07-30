from __future__ import annotations

from prompt_toolkit.application import Application
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.containers import Window

from .base import BasePrompt


class Expand(BasePrompt):
    """Inquirer-style expand prompt."""

    def __init__(
        self,
        message: str,
        choices: dict[str, str],
        *,
        theme=None,
    ) -> None:
        super().__init__(
            message,
            theme=theme,
        )

        if not choices:
            raise ValueError("choices cannot be empty")

        self.choices = choices
        self.key = ""
        self.selected = None

    def render(self):
        keys = "".join(self.choices.keys())

        parts = [
            (
                self.theme.pointer_style,
                f"{self.theme.pointer} ",
            ),
            (
                self.theme.message_style,
                f"{self.message}: ({keys}) ",
            ),
            (
                self.theme.pointer_style,
                self.key,
            ),
        ]

        if self.selected:
            parts.append(
                (
                    self.theme.muted_style,
                    f"\n{self.key}: {self.selected}",
                )
            )

        return FormattedText(parts)

    def ask(self):
        control = FormattedTextControl(
            self.render,
            focusable=True,
        )

        window = Window(
            content=control,
        )

        bindings = KeyBindings()

        @bindings.add("enter")
        def _(event):
            if self.selected:
                event.app.exit(result=self.selected)

        @bindings.add("c-c")
        def _(event):
            event.app.exit(result=None)

        @bindings.add("<any>")
        def _(event):
            key = event.key_sequence[0].key

            if len(key) != 1:
                return

            if key not in self.choices:
                return

            self.key = key
            self.selected = self.choices[key]

            event.app.invalidate()

        app = Application(
            layout=Layout(window),
            key_bindings=bindings,
            style=self.theme.style(),
            full_screen=False,
        )

        return app.run()
