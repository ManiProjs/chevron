from __future__ import annotations

from prompt_toolkit.shortcuts import print_formatted_text

from .base import BasePrompt


class Expand(BasePrompt):
    """Single-key selection prompt."""

    def __init__(
        self,
        message: str,
        choices: dict[str, str],
        *,
        default: str | None = None,
        theme=None,
    ) -> None:
        super().__init__(
            message,
            theme=theme,
        )

        if not choices:
            raise ValueError("choices cannot be empty")

        self.choices = choices
        self.default = default

        if default and default not in choices:
            raise ValueError("default must be one of the choice keys")

    def ask(self) -> str:
        print_formatted_text(
            self.renderer.expand(
                self.message,
                self.choices,
                self.default,
            )
        )

        while True:
            key = self.terminal.key()

            if key == "\x03":
                raise KeyboardInterrupt

            if key in self.choices:
                answer = self.choices[key]

                print_formatted_text(self.renderer.success(answer))

                return answer

            if key == "\r" and self.default:
                answer = self.choices[self.default]

                print_formatted_text(self.renderer.success(answer))

                return answer
