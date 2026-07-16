from __future__ import annotations

from collections.abc import Callable

from .base import BasePrompt


class Password(BasePrompt):
    """Prompt the user for a password."""

    def __init__(
        self,
        message: str,
        *,
        validator: Callable[[str], bool] | None = None,
        theme=None,
    ):
        super().__init__(message, theme=theme)
        self.validator = validator

    def ask(self) -> str:
        while True:
            value = self.terminal.input(
                self.renderer.prompt(self.message),
                password=True,
            )

            if self.validator and not self.validator(value):
                self.renderer.error("Invalid password.")
                continue

            return value
