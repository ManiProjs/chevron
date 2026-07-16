from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from .base import BasePrompt


class Editor(BasePrompt):
    def __init__(
        self,
        message: str,
        *,
        default: str = "",
        file_extension: str = "",
        editor: str | None = None,
        theme=None,
    ):
        super().__init__(message, theme=theme)
        self.default = default
        self.file_extension = file_extension
        self.editor = editor or self._find_editor()

    def _find_editor(self) -> str:
        for name in (
            os.environ.get("VISUAL"),
            os.environ.get("EDITOR"),
            "nano",
            "vi",
        ):
            if name and (shutil.which(name.split()[0]) or Path(name).exists()):
                return name

        raise RuntimeError("No editor found. Set the EDITOR environment variable.")

    def ask(self) -> str:
        suffix = self.file_extension

        with tempfile.NamedTemporaryFile(
            mode="w+",
            suffix=suffix,
            delete=False,
        ) as file:
            path = Path(file.name)
            file.write(self.default)
            file.flush()

        try:
            subprocess.run(
                [*self.editor.split(), str(path)],
                check=True,
            )

            return path.read_text()
        finally:
            path.unlink(missing_ok=True)
