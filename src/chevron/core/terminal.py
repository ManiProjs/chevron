from __future__ import annotations

from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import AnyFormattedText


class Terminal:
    """Thin wrapper around prompt_toolkit."""

    def input(
        self,
        prompt_text: AnyFormattedText = "",
        *,
        password: bool = False,
    ) -> str:
        return prompt(
            prompt_text,
            is_password=password,
        )

    def clear(self) -> None:
        print("\033[2J\033[H", end="")

    def hide_cursor(self) -> None:
        print("\033[?25l", end="", flush=True)

    def show_cursor(self) -> None:
        print("\033[?25h", end="", flush=True)
