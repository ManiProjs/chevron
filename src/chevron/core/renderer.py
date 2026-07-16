from __future__ import annotations

from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.shortcuts import print_formatted_text

from ..theme.theme import Theme


class Renderer:
    def __init__(self, theme: Theme):
        self.theme = theme

    def prompt(self, message: str):
        lines = message.split("\n")

        if len(lines) > 1 and lines[0] == "":
            lines = lines[1:]

        if len(lines) > 1:
            return FormattedText([
                (self.theme.error_style, lines[0]),
                ("", "\n"),
                (self.theme.pointer_style, self.theme.pointer),
                ("", " "),
                (self.theme.message_style, "\n".join(lines[1:])),
                ("", "\n> "),
            ])

        return FormattedText([
            (self.theme.pointer_style, self.theme.pointer),
            ("", " "),
            (self.theme.message_style, message),
            ("", "\n> "),
        ])

    def search(self, message: str, query: str, choices: list[str]):
        parts = [
            (self.theme.pointer_style, self.theme.pointer),
            ("", " "),
            (self.theme.message_style, message),
            ("", "\n> "),
            ("", query),
        ]

        if choices:
            parts.append(("", "\n"))

            for index, choice in enumerate(choices):
                if index == 0:
                    parts.append((self.theme.pointer_style, ">> "))
                else:
                    parts.append(("", "   "))

                parts.append((self.theme.message_style, choice))

                if index != len(choices) - 1:
                    parts.append(("", "\n"))

            parts.append(("", "\n> "))

        return FormattedText(parts)

    def success(self, message: str):
        print_formatted_text(
            FormattedText([
                (self.theme.success_style, "✔ "),
                (self.theme.success_style, message),
            ])
        )

    def error(self, message: str):
        return FormattedText([
            (self.theme.error_style, "✖ "),
            (self.theme.error_style, message),
        ])
