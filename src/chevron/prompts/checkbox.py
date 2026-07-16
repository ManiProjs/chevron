from .list import ListPrompt


class Checkbox(ListPrompt):
    def __init__(self, message: str, choices: list[str], *, theme=None):
        super().__init__(message, choices, theme=theme)
        self.selected: set[int] = set()

    def render(self):
        lines = [
            (self.theme.pointer_style, f"{self.theme.pointer} "),
            (self.theme.message_style, self.message),
            ("", "\n\n"),
        ]

        for i, choice in enumerate(self.choices):
            current = i == self.index
            checked = "[x]" if i in self.selected else "[ ]"
            style = self.theme.selected_style if current else ""
            prefix = f"{self.theme.pointer} " if current else "  "
            lines.append((style, f"{prefix}{checked} {choice.title}\n"))

        lines.append(
            (self.theme.footer_style, "\n↑↓ Navigate • Space Toggle • Enter Confirm")
        )
        return lines

    def ask(self) -> list[str]:
        @self._bindings.add(" ")
        def _(event):
            if self.index in self.selected:
                self.selected.remove(self.index)
            else:
                self.selected.add(self.index)

        @self._bindings.add("enter")
        def _(event):
            self._result = [
                self.choices[i].value
                for i in range(len(self.choices))
                if i in self.selected
            ]
            event.app.exit()

        return self.run()
