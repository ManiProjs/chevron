import pytest
from unittest.mock import MagicMock
from chevron.prompts.confirm import Confirm
from chevron.theme.theme import Theme

# --- Fixtures for Setup ---

@pytest.fixture
def mock_terminal():
    """Fixture to mock the terminal input/output."""
    mock = MagicMock()
    return mock

@pytest.fixture
def mock_renderer():
    """Fixture to mock the renderer, which handles prompt formatting."""
    mock = MagicMock()
    # We assume self.renderer.prompt returns a string for simplicity in testing flow
    mock.prompt.return_value = "Prompt text here"
    return mock

@pytest.fixture
def theme_default():
    """A default theme object for testing."""
    return Theme(accent="#60A5FA", error="#EF4444")

# --- Test Cases for Confirm Prompt Logic ---

def test_confirm_default_yes(mock_terminal, mock_renderer):
    """Test confirmation defaults to True when the user enters nothing (empty input)."""
    # Mock terminal.input to return an empty string, simulating user pressing Enter immediately.
    mock_terminal.input.return_value = ""

    prompt = Confirm("Are you sure?", default=True)
    result = prompt.ask()

    assert result is True

def test_confirm_default_no(mock_terminal, mock_renderer):
    """Test confirmation defaults to False when the user enters nothing (empty input)."""
    # Mock terminal.input to return an empty string
    mock_terminal.input.return_value = ""

    prompt = Confirm("Are you sure?", default=False)
    result = prompt.ask()

    assert result is False

def test_confirm_yes(mock_terminal, mock_renderer):
    """Test confirmation returns True when user inputs 'y' or 'yes'."""
    mock_terminal.input.return_value = "Yes"

    prompt = Confirm("Are you sure?", default=False)
    result = prompt.ask()

    assert result is True

def test_confirm_no(mock_terminal, mock_renderer):
    """Test confirmation returns False when user inputs 'n' or 'no'."""
    mock_terminal.input.return_value = "No"

    prompt = Confirm("Are you sure?", default=True)
    result = prompt.ask()

    assert result is False

def test_confirm_with_theme_style(mock_terminal, mock_renderer, theme_default):
    """Test that the prompt correctly applies style based on the theme."""
    # This test focuses on ensuring the instantiation works and theme is passed correctly.

    prompt = Confirm("Confirm action", default=True, theme=theme_default)

    assert prompt.theme is theme_default
