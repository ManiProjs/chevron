from __future__ import annotations

from .renderer import Renderer
from .terminal import Terminal
from ..theme.theme import Theme


class Session:
    """Holds shared objects used while a prompt is active."""

    def __init__(self, theme: Theme) -> None:
        self.theme = theme
        self.terminal = Terminal()
        self.renderer = Renderer(theme)
