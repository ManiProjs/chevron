from __future__ import annotations

from .prompts.input import Input
from .prompts.password import Password
from .prompts.confirm import Confirm
from .prompts.select import Select
from .prompts.checkbox import Checkbox
from .theme.theme import Theme


class Chevron:
    """High-level interface for interactive terminal prompts."""

    def __init__(self, theme: Theme | None = None):
        self.theme = theme or Theme()

    def input(self, message: str, **kwargs):
        return Input(message, theme=self.theme, **kwargs).ask()

    def password(self, message: str, **kwargs):
        return Password(message, theme=self.theme, **kwargs).ask()

    def confirm(self, message: str, **kwargs):
        return Confirm(message, theme=self.theme, **kwargs).ask()

    def select(self, message: str, choices: list[str], **kwargs):
        return Select(
            message,
            choices,
            theme=self.theme,
            **kwargs,
        ).ask()

    def checkbox(self, message: str, choices: list[str], **kwargs):
        return Checkbox(
            message,
            choices,
            theme=self.theme,
            **kwargs,
        ).ask()
