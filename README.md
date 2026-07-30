# Chevron

[![PyPI](https://img.shields.io/pypi/v/chevron-sh.svg)](https://pypi.org/project/chevron/)
[![Python](https://img.shields.io/pypi/pyversions/chevron-sh.svg)](https://pypi.org/project/chevron/)
[![License](https://img.shields.io/github/license/ManiProjs/chevron)](LICENSE)
[![CI](https://github.com/ManiProjs/chevron/actions/workflows/ci.yml/badge.svg)](https://github.com/ManiProjs/chevron/actions/workflows/ci.yml)

> Beautiful, modern interactive terminal prompts for Python.

Chevron is a modern prompt library built on top of `prompt_toolkit`. It provides a clean API for creating beautiful CLI experiences with customizable themes, interactive controls, and reusable terminal components.

## Features

- 🎨 Modern terminal UI
- ⚡ Powered by `prompt_toolkit`
- 📝 Text input
- 🔒 Password input
- ✅ Confirmation prompts
- 🔢 Number prompts
- 🎯 Select menus
- ☑️ Checkbox prompts
- 🔍 Interactive search
- ✏️ Editor prompts
- 🔀 Expand prompts
- ⏳ Spinner controls
- 🌈 Theme customization

## Installation

```bash
pip install chevron
```

or:

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
    ],
).ask()

remember = Confirm(
    "Remember your choice?"
).ask()
```

## Prompts

### Input

```python
Input("Name").ask()
```

### Password

```python
Password("Password").ask()
```

### Confirm

```python
Confirm("Delete project?").ask()
```

### Number

```python
Number("Age").ask()
```

### Select

```python
Select(
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
Checkbox(
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
Search(
    "Search package",
    [
        "numpy",
        "pandas",
        "torch",
    ],
).ask()
```

### Expand

Inquirer-style single-key selection:

```python
Expand(
    "Choose an action",
    {
        "n": "Create a new file",
        "o": "Open a file",
        "d": "Delete a file",
        "q": "Quit",
    },
).ask()
```

Example:

```text
❯ Choose an action: (nodq) o
o: Open a file
```

### Editor

```python
Editor(
    "Commit message"
).ask()
```

## Themes

Chevron supports customizable themes:

```python
from chevron import Theme, Input

theme = Theme(
    pointer="▶",
)

Input(
    "Name",
    theme=theme,
).ask()
```

Themes control:

- icons
- colors
- prompt styles
- selected states
- messages

## Examples

```bash
python examples/input.py
python examples/select.py
python examples/checkbox.py
python examples/search.py
python examples/expand.py
python examples/all.py
```

## Roadmap

### Completed

- [x] Input prompt
- [x] Password prompt
- [x] Confirm prompt
- [x] Number prompt
- [x] Select prompt
- [x] Checkbox prompt
- [x] Search prompt
- [x] Editor prompt
- [x] Expand prompt
- [x] Theme system

### Planned

- [ ] Unit tests
- [ ] Async API
- [ ] Plugin system
- [ ] Custom prompt API
- [ ] More terminal controls

## Contributing

Contributions, ideas, bug reports, and pull requests are welcome.

## License

MIT License.