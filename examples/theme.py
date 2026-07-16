from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Theme:
    """Visual theme used by Chevron prompts."""

    # Symbols
    pointer: str = "❯"
    success_icon: str = "✔"
    error_icon: str = "✖"
    warning_icon: str = "⚠"
    info_icon: str = "ℹ"

    # Colors
    accent: str = "#60A5FA"
    success: str = "#22C55E"
    error: str = "#EF4444"
    warning: str = "#F59E0B"
    info: str = "#06B6D4"

    # Styles (prompt_toolkit style strings)
    pointer_style: str = "bold fg:#60A5FA"
    message_style: str = ""
    selected_style: str = "bold fg:#60A5FA"
    success_style: str = "bold fg:#22C55E"
    error_style: str = "bold fg:#EF4444"
    warning_style: str = "bold fg:#F59E0B"
    info_style: str = "bold fg:#06B6D4"

    # Borders
    border: str = "rounded"
