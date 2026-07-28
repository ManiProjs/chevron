from __future__ import annotations

import time
from itertools import cycle

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl

from chevron.ui.control import PromptControl


class SpinnerControl(PromptControl):
    FRAMES = (
        "⠋",
        "⠙",
        "⠹",
        "⠸",
        "⠼",
        "⠴",
        "⠦",
        "⠧",
        "⠇",
        "⠏",
    )

    def __init__(
        self,
        message: str,
        theme,
    ):
        self.message = message
        self.theme = theme

        self.running = True
        self.frame = cycle(self.FRAMES)

        self._window = Window(
            FormattedTextControl(self.render),
            height=1,
        )

        self._bindings = KeyBindings()

        @self._bindings.add("c-c")
        @self._bindings.add("escape")
        def _(event):
            self.running = False
            event.app.exit(result=None)

    @property
    def window(self):
        return self._window

    @property
    def key_bindings(self):
        return self._bindings

    def render(self):
        return [
            (
                self.theme.pointer_style,
                f"{next(self.frame)} {self.message}",
            )
        ]

    def tick(self):
        time.sleep(0.08)
