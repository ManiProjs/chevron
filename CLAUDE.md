# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Setup
To install dependencies:
```bash
pip install chevron
```

### Running Tests
To run the test suite:
```bash
pytest
```

### Running Examples
The following commands can run the examples provided in `examples/` directory:
```bash
python examples/input.py
python examples/select.py
python examples/all.py
```

## Code Architecture and Structure

The project is a Python package built on top of `prompt_toolkit`. The core library is within the `chevron` package.

**Core Structure:**
- **`chevron/`**: Contains the main package code, including prompt classes, themes, and input handlers.
    - **Prompts (`prompts/`)**: Defines specific interactive prompt classes (e.g., `checkbox.py`).
    - **Themes (`theme/`)**: Manages terminal appearance and styling.
    - **UI Components**: Classes that handle user interaction logic (Input, Select, Confirm, Checkbox).

**Key Architectural Insight:**
The library is structured around the separation of concerns:
1. **Interaction Layer**: The public classes (e.g., `Input`, `Select`) handle reading from the terminal and managing user input flow.
2. **Presentation Layer**: Themes control *how* the interaction looks.
3. **Composition**: Prompts are composed by wrapping I/O components with specific theme settings, allowing for highly customizable, pluggable UI elements.

**To understand the full architecture:**
- Focus on how `Input`, `Select`, `Confirm`, and `Checkbox` classes interact with the `Theme` class to see how themes influence prompt behavior.
- Look at the dependencies between files in `prompts/` and `theme/` to trace how configuration flows from a theme settings down to the prompt execution.

## External Context
The repository includes:
- **`README.md`**: Contains installation instructions and basic usage examples.
- **`LICENSE`**: Specifies the project license.