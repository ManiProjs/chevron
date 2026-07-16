

from chevron import Search


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