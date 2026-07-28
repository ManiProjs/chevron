from chevron import Search
from chevron.ui.search_control import SearchItem


packages = [
    "numpy",
    "pandas",
    "requests",
    "torch",
    "tensorflow",
    "matplotlib",
]


package = Search(
    "Search package",
    packages,
).ask()

print(f"Selected: {package}")

pacman = Search(
    "Choose your package manager",
    [
        SearchItem(
            value="pip", label="pip", description="Python's default package manager"
        ),
        SearchItem(
            value="poetry", label="Poetry", description="A good package manager"
        ),
        SearchItem(
            value="uv", label="uv", description="An even better package manager"
        ),
    ],
).ask()

print(f"Selected: {pacman}")
