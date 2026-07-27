from chevron.core.runner import PromptRunner
from chevron.ui.search_control import SearchControl

from .base import BasePrompt


class Search(BasePrompt):
    def __init__(
        self,
        message: str,
        choices,
        *,
        default: str = "",
        theme=None,
    ) -> None:
        super().__init__(
            message,
            theme=theme,
        )

        self.choices = choices
        self.default = default

    def ask(self):
        control = SearchControl(
            message=self.message,
            choices=self.choices,
            theme=self.theme,
        )

        if self.default:
            control.input.text = self.default

        return PromptRunner(self.theme).run(control)
