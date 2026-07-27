from __future__ import annotations

from abc import ABC, abstractmethod
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import Container


class PromptControl(ABC):
    @property
    @abstractmethod
    def window(self) -> Container:
        pass

    @property
    @abstractmethod
    def key_bindings(self) -> KeyBindings:
        pass
