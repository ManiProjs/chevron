from __future__ import annotations

from prompt_toolkit.formatted_text import FormattedText

from .base import BasePrompt


class Confirm(BasePrompt):
    """Yes/No prompt."""

    def __init__(
        self,
        message: str,
        *,
        default: bool = True,
        theme=None,
    ):
        super().__init__(message, theme=theme)
        self.default = default

    def ask(self) -> bool:
        suffix = "Y/n" if self.default else "y/N"

        while True:
            prompt = FormattedText([
                *self.renderer.prompt(self.message),
                ("", f" ({suffix}) "),
            ])

            value = (
                self.terminal.input(prompt)
                .strip()
                .lower()
            )

            if value == "":
                return self.default

            if value in ("y", "yes"):
                return True

            if value in ("n", "no"):
                return False

            self.renderer.error("Please answer yes or no.")
