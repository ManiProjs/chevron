from __future__ import annotations

from .base import BasePrompt


class Number(BasePrompt):
    """Prompt the user for a number."""

    def __init__(
        self,
        message: str,
        *,
        default: int | float | None = None,
        minimum: int | float | None = None,
        maximum: int | float | None = None,
        integer: bool = False,
        theme=None,
    ) -> None:
        super().__init__(message, theme=theme)

        self.default = default
        self.minimum = minimum
        self.maximum = maximum
        self.integer = integer

    def ask(self) -> int | float:
        while True:
            value = self.terminal.input(self.renderer.prompt(self.message)).strip()

            if value == "" and self.default is not None:
                return self.default

            try:
                number = int(value) if self.integer else float(value)
            except ValueError:
                self.renderer.error("Please enter a valid number.")
                continue

            if self.minimum is not None and number < self.minimum:
                self.renderer.error(f"Number must be at least {self.minimum}.")
                continue

            if self.maximum is not None and number > self.maximum:
                self.renderer.error(f"Number must be at most {self.maximum}.")
                continue

            return number
