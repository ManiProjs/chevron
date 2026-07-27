from __future__ import annotations

from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout


class PromptRunner:
    def __init__(self, theme):
        self.theme = theme

    def run(self, control):
        app = Application(
            layout=Layout(control.window),
            key_bindings=control.key_bindings,
            style=self.theme.style(),
            mouse_support=False,
            full_screen=False,
        )

        try:
            return app.run()
        except KeyboardInterrupt:
            return None
