# Chevron

[![PyPI](https://img.shields.io/pypi/v/chevron-sh.svg)](https://pypi.org/project/chevron/)
[![Python](https://img.shields.io/pypi/pyversions/chevron-sh.svg)](https://pypi.org/project/chevron/)
[![License](https://img.shields.io/github/license/ManiProjs/chevron)](LICENSE)
[![CI](https://github.com/ManiProjs/chevron/actions/workflows/ci.yml/badge.svg)](https://github.com/ManiProjs/chevron/actions/workflows/ci.yml)

> Beautiful, modern interactive terminal prompts for Python.

Chevron is a modern prompt library for Python built on top of `prompt_toolkit`. It helps you build beautiful interactive command-line applications with a clean, intuitive API, rich terminal controls, and customizable themes.

## Features

- 🎨 Modern terminal UI
- ⚡ Powered by `prompt_toolkit`
- 📝 Text input
- 🔒 Password input
- ✅ Confirmation prompts
- ☑️ Checkbox prompts
- 🔍 Interactive search prompt
- 📝 Built-in text editor
- 🎯 Consistent keyboard navigation
- 🌈 Theme support
- 🚀 Fast and lightweight

## Installation

```bash
pip install chevron
```

Or with uv:

```bash
uv add chevron
```

## Quick Start

```python
from chevron import Input, Select, Confirm

name = Input("What's your name?").ask()

language = Select(
    "Favorite language",
    [
        "Python",
        "Rust",
        "Go",
        "Zig",
    ],
).ask()

remember = Confirm(
    "Remember your choice?"
).ask()

print(name)
print(language)
print(remember)
```

## Available Prompts

### Input

```python
name = Input("Name").ask()
```

### Password

```python
password = Password("Password").ask()
```

### Confirm

```python
delete = Confirm(
    "Delete project?"
).ask()
```

### Select

```python
language = Select(
    "Language",
    [
        "Python",
        "Rust",
        "Go",
    ],
).ask()
```

### Checkbox

```python
languages = Checkbox(
    "Languages",
    [
        "Python",
        "Rust",
        "Go",
    ],
).ask()
```

### Search

```python
package = Search(
    "Search package",
    [
        "numpy",
        "pandas",
        "matplotlib",
        "torch",
    ],
).ask()
```

### Editor

```python
text = Editor(
    "Commit message"
).ask()
```

## Themes

```python
from chevron import Theme

theme = Theme(
    pointer="▶",
)

Input(
    "Name",
    theme=theme,
).ask()
```

## Examples

Run the examples:

```bash
python examples/input.py
python examples/select.py
python examples/all.py
```

## Roadmap

- [x] Input
- [x] Password
- [x] Confirm
- [x] Number
- [x] Select improvements
- [x] Checkbox improvements
- [x] Search prompt
- [ ] Unit tests
- [ ] Async API
- [ ] Plugin system

## Contributing

Contributions, ideas, bug reports, and pull requests are welcome.

## License

MIT License.
