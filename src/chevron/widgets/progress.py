from __future__ import annotations

import sys
from time import perf_counter

from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.shortcuts import print_formatted_text

from ..theme.theme import Theme


class Progress:
    """Terminal progress bar widget."""

    def __init__(
        self,
        total: int,
        description: str = "",
        *,
        width: int = 30,
        theme: Theme | None = None,
    ):
        if total <= 0:
            raise ValueError("total must be greater than zero")

        self.total = total
        self.completed = 0

        self.description = description
        self.width = width

        self.theme = theme or Theme()

        self.start_time = perf_counter()
        self.finished = False

    @property
    def ratio(self):
        return self.completed / self.total

    @property
    def percent(self):
        return int(self.ratio * 100)

    @property
    def elapsed(self):
        return perf_counter() - self.start_time

    @property
    def speed(self):
        if self.elapsed == 0:
            return 0

        return self.completed / self.elapsed

    @property
    def eta(self):
        if self.speed == 0:
            return 0

        remaining = self.total - self.completed
        return remaining / self.speed

    def advance(self, amount: int = 1):
        self.update(self.completed + amount)

    def update(self, value: int):
        self.completed = max(
            0,
            min(value, self.total),
        )

        self.render()

    def format_time(self, seconds: float):
        seconds = int(seconds)

        minutes, seconds = divmod(seconds, 60)

        if minutes:
            return f"{minutes:02d}:{seconds:02d}"

        return f"{seconds:02d}s"

    def render(self):
        filled = int(self.width * self.ratio)

        bar = "█" * filled + "░" * (self.width - filled)

        eta = self.format_time(self.eta)

        parts = [
            (self.theme.message_style, self.description),
            ("", " "),
            (self.theme.pointer_style, "["),
            (self.theme.success_style, bar[:filled]),
            (self.theme.message_style, bar[filled:]),
            (self.theme.pointer_style, "]"),
            ("", f" {self.percent:3d}%"),
            ("", f" {self.completed}/{self.total}"),
            ("", f" • {self.speed:.1f}/s"),
            ("", f" • ETA {eta}"),
        ]

        text = FormattedText(parts)

        sys.stdout.write("\r")
        print_formatted_text(text, end="")
        sys.stdout.flush()

    def finish(self):
        self.completed = self.total
        self.render()
        print()
        self.finished = True

    def __enter__(self):
        self.render()
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.finish()
