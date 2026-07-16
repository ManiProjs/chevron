from __future__ import annotations

from .list import ListPrompt


class Select(ListPrompt):
    def __init__(self, message: str, choices: list[str], *, theme=None):
        super().__init__(message, choices, theme=theme)

    def ask(self):
        @self._bindings.add("enter")
        def _(event):
            self._result = self.choices[self.index]
            event.app.exit()

        return self.run()
