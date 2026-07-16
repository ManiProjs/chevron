from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True, frozen=True)
class Choice:
    """Represents a selectable choice in list-based prompts."""

    title: str
    value: Any | None = None
    disabled: bool = False
    description: str | None = None

    def __post_init__(self):
        if self.value is None:
            object.__setattr__(self, "value", self.title)

    @property
    def is_disabled(self) -> bool:
        return self.disabled

    def with_value(self, value: Any) -> "Choice":
        return Choice(
            title=self.title,
            value=value,
            disabled=self.disabled,
            description=self.description,
        )

    def disable(self) -> "Choice":
        return Choice(
            title=self.title,
            value=self.value,
            disabled=True,
            description=self.description,
        )

    def enable(self) -> "Choice":
        return Choice(
            title=self.title,
            value=self.value,
            disabled=False,
            description=self.description,
        )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return (
            f"Choice(title={self.title!r}, "
            f"value={self.value!r}, "
            f"disabled={self.disabled!r})"
        )
