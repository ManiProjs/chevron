from __future__ import annotations

from collections.abc import Callable

from .base import BasePrompt


class Input(BasePrompt):
    """Prompt the user for text."""

    def __init__(
        self,
        message: str,
        *,
        default: str = "",
        validator: Callable[[str], str | bool | None] | None = None,
        transform: Callable[[str], str] | None = None,
        required: bool = False,
        theme=None,
    ) -> None:
        super().__init__(message, theme=theme)

        self.default = default
        self.validator = validator
        self.transform = transform
        self.required = required

    def ask(self) -> str:
        error = None

        while True:
            message = self.message

            if error is not None:
                message = f"\n{error}\n{message}"

            prompt = self.renderer.prompt(message)
            self.rendered_lines = prompt.count("\n") + 1

            value = self.terminal.input(prompt)
            self.rendered_lines += 1

            if not value:
                value = self.default

            if self.transform is not None:
                value = self.transform(value)

            if self.required and not value:
                self.clear_prompt()
                self.rendered_lines = 0
                error = "✖ This field is required."
                continue

            if self.validator is not None:
                validation_result = self.validator(value)

                if validation_result is False:
                    self.clear_prompt()
                    self.rendered_lines = 0
                    error = "✖ Invalid input."
                    continue

                if isinstance(validation_result, str):
                    self.clear_prompt()
                    self.rendered_lines = 0
                    error = f"✖ {validation_result}"
                    continue

            self.clear_prompt()
            return value
