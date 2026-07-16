"""Temporary query/refinement prompt implementation.
Not an interactive search widget.
"""

from __future__ import annotations

from typing import Sequence, Optional

from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.controls import UIControl, UIContent
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.dimension import Dimension
from prompt_toolkit.mouse_events import MouseEvent
from prompt_toolkit.formatted_text import StyleAndTextTuples
from prompt_toolkit.styles import Style
from prompt_toolkit.data_structures import Point


class SearchControl:
    """Interactive search UI using a custom UIControl."""

    def __init__(self, message: str, choices: Sequence[str], theme) -> None:
        self.message = message
        self.choices = list(choices)
        self.theme = theme
        self.result: Optional[str] = None

    def run(self) -> Optional[str]:
        control = _SearchControl(
            message=self.message,
            choices=self.choices,
            theme=self.theme,
        )
        window = Window(
            content=control,
            height=Dimension(preferred=6, min=6, max=6),
            wrap_lines=False,
            dont_extend_height=True,
            style="class:searchcontrol",
            always_hide_cursor=False,
        )

        style = Style.from_dict({
            'pointer': self.theme.pointer_style,
            'message': self.theme.message_style,
            'selected': self.theme.pointer_style,
            'query': '',
        })

        kb = control.get_key_bindings()

        app = Application(
            layout=Layout(window),
            key_bindings=kb,
            mouse_support=True,
            style=style,
            full_screen=False,
        )

        try:
            result = app.run()
        except KeyboardInterrupt:
            result = None

        self.result = result
        return result


class _SearchControl(UIControl):
    def __init__(self, message: str, choices: Sequence[str], theme) -> None:
        self.message = message
        self.choices = choices
        self.theme = theme

        self.query = ""
        self.selected = 0
        self.scroll_offset = 0
        self.matches = self._filter_matches()
        self._done = False
        self._result: Optional[str] = None

    def _filter_matches(self) -> list[str]:
        q = self.query.lower()
        if not q:
            return self.choices
        return [c for c in self.choices if q in c.lower()]

    def create_content(self, width: int, height: int) -> UIContent:
        lines: StyleAndTextTuples = []

        # First line: pointer + message
        lines.append([
            ('class:pointer', self.theme.pointer),
            ('class:message', f' {self.message}'),
        ])

        # Second line: '> ' + query (editable)
        lines.append([
            ('class:message', '> '),
            ('class:query', self.query),
        ])

        # Reserve 2 lines for the prompt and query, leaving 4 visible results.
        visible_height = 4

        if self.selected < self.scroll_offset:
            self.scroll_offset = self.selected
        elif self.selected >= self.scroll_offset + visible_height:
            self.scroll_offset = self.selected - visible_height + 1

        visible_matches = self.matches[
            self.scroll_offset:self.scroll_offset + visible_height
        ]

        for offset, match in enumerate(visible_matches):
            i = self.scroll_offset + offset
            if i == self.selected:
                lines.append([
                    ('class:selected', self.theme.pointer),
                    ('', ' '),
                    ('class:selected', match),
                ])
            else:
                lines.append([
                    ('', '  '),
                    ('', match),
                ])

        def get_line(i: int):
            if i < len(lines):
                return lines[i]
            else:
                return []

        return UIContent(
            get_line=get_line,
            line_count=max(6, len(lines)),
            show_cursor=True,
            cursor_position=Point(x=2, y=1),
        )

    def is_focusable(self) -> bool:
        return True

    def get_key_bindings(self) -> KeyBindings:
        kb = KeyBindings()

        @kb.add('c-c')
        @kb.add('escape')
        def _(event):
            # Cancel search
            event.app.exit(result=None)

        @kb.add('enter')
        def _(event):
            # Accept current selection if any
            if self.matches:
                event.app.exit(result=self.matches[self.selected])
            else:
                event.app.exit(result=None)

        @kb.add('up')
        def _(event):
            if self.matches:
                self.selected = (self.selected - 1) % len(self.matches)
                event.app.invalidate()

        @kb.add('down')
        def _(event):
            if self.matches:
                self.selected = (self.selected + 1) % len(self.matches)
                event.app.invalidate()

        @kb.add('backspace')
        def _(event):
            if self.query:
                self.query = self.query[:-1]
                self._update_matches(event)

        @kb.add('<any>')
        def _(event):
            # Printable characters append to query
            if event.data and event.data.isprintable():
                self.query += event.data
                self._update_matches(event)

        return kb

    def _update_matches(self, event):
        self.matches = self._filter_matches()
        if self.selected >= len(self.matches):
            self.selected = max(0, len(self.matches) - 1)
        max_offset = max(0, len(self.matches) - 1)
        self.scroll_offset = min(self.scroll_offset, max_offset)
        event.app.invalidate()

    def mouse_handler(self, mouse_event: MouseEvent):
        # No mouse support for now
        return NotImplemented