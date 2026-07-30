from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import AnyFormattedText

from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.controls import DummyControl
from prompt_toolkit.layout.containers import Window


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

    def read_key(self) -> str:
        result = []

        bindings = KeyBindings()

        @bindings.add("<any>")
        def _(event):
            result.append(event.key_sequence[0].key)
            event.app.exit()

        app = Application(
            layout=Layout(Window(DummyControl())),
            key_bindings=bindings,
            full_screen=False,
        )

        app.run()

        if not result:
            return ""

        return result[0]

    def clear(self) -> None:
        print("\033[2J\033[H", end="")

    def hide_cursor(self) -> None:
        print("\033[?25l", end="", flush=True)

    def show_cursor(self) -> None:
        print("\033[?25h", end="", flush=True)
