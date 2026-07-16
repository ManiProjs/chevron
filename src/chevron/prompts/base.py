from __future__ import annotations

from abc import ABC, abstractmethod

from ..core.renderer import Renderer
from ..core.terminal import Terminal
from ..theme.theme import Theme


class BasePrompt(ABC):
    """Base class for every Chevron prompt."""

    def __init__(
        self,
        message: str,
        *,
        theme: Theme | None = None,
    ) -> None:
        self.message = message
        self.theme = theme or Theme()

        self.terminal = Terminal()
        self.renderer = Renderer(self.theme)
        self.rendered_lines = 0

    def clear_prompt(self):
        for _ in range(self.rendered_lines):
            print("\033[2K\033[1A", end="")

        print("\033[2K", end="")
        self.rendered_lines = 0

    @abstractmethod
    def ask(self):
        raise NotImplementedError
