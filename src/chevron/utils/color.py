from __future__ import annotations

import re


ANSI_COLORS = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
}


def apply_style(style: str, text: str) -> str:
    codes: list[str] = []

    if "bold" in style:
        codes.append("1")

    match = re.search(r"fg:#([0-9a-fA-F]{6})", style)

    if match:
        r = int(match.group(1)[0:2], 16)
        g = int(match.group(1)[2:4], 16)
        b = int(match.group(1)[4:6], 16)

        codes.append(f"38;2;{r};{g};{b}")

    if not codes:
        return text

    return f"\033[{';'.join(codes)}m{text}\033[0m"
