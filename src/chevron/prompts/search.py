from typing import Sequence

from chevron.ui.search_control import SearchControl

from .base import BasePrompt


class Search(BasePrompt):
    def __init__(
        self,
        message: str,
        choices: Sequence[str],
        *,
        default: str = "",
        theme=None,
    ) -> None:
        super().__init__(message, theme=theme)
        self.message = message
        self.choices = list(choices)
        self.default = default

    def ask(self) -> str | None:
        control = SearchControl(
            message=self.message,
            choices=self.choices,
            theme=self.theme,
        )
        control.query = self.default
        return control.run()
