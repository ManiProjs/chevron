from dataclasses import dataclass


@dataclass(slots=True)
class Theme:
    pointer: str = "❯"

    accent: str = "#60A5FA"
    success: str = "#22C55E"
    error: str = "#EF4444"
    warning: str = "#F59E0B"

    pointer_style: str = "bold fg:#60A5FA"
    message_style: str = "bold"
    selected_style: str = "bold fg:#60A5FA"
    footer_style: str = "fg:#6B7280 italic"
    success_style: str = "bold fg:#22C55E"
    error_style: str = "bold fg:#EF4444"
    warning_style: str = "bold fg:#F59E0B"
    info_style: str = "bold fg:#06B6D4"
