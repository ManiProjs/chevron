from __future__ import annotations

import sys
import threading
import time
from itertools import cycle

from ..theme.theme import Theme
from ..utils.color import apply_style


class Spinner:
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
        *,
        interval: float = 0.08,
        theme: Theme | None = None,
    ) -> None:
        self.message = message
        self.interval = interval
        self.theme = theme or Theme()

        self._running = False
        self._thread: threading.Thread | None = None
        self._lock = threading.Lock()

    def _write(self, style: str, text: str) -> None:
        sys.stdout.write(apply_style(style, text))
        sys.stdout.flush()

    def _clear_line(self) -> None:
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()

    def _render(self, frame: str) -> None:
        self._clear_line()

        self._write(
            self.theme.pointer_style,
            frame,
        )

        sys.stdout.write(" ")

        self._write(
            self.theme.message_style,
            self.message,
        )

        sys.stdout.flush()

    def _run(self) -> None:
        for frame in cycle(self.FRAMES):
            with self._lock:
                if not self._running:
                    break

            self._render(frame)
            time.sleep(self.interval)

    def start(self) -> None:
        with self._lock:
            if self._running:
                return

            self._running = True

        self._thread = threading.Thread(
            target=self._run,
            daemon=True,
        )

        self._thread.start()

    def stop(
        self,
        *,
        success: bool = True,
        message: str | None = None,
    ) -> None:
        with self._lock:
            if not self._running:
                return

            self._running = False

        if self._thread:
            self._thread.join()

        self._clear_line()

        icon = self.theme.success_icon if success else self.theme.error_icon

        style = self.theme.success_style if success else self.theme.error_style

        final_message = message or self.message

        self._write(
            style,
            f"{icon} {final_message}",
        )

        sys.stdout.write("\n")
        sys.stdout.flush()
