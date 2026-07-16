from chevron import Checkbox

languages = Checkbox(
    "Languages you know",
    [
        "Python",
        "Rust",
        "Go",
        "Zig",
    ],
).ask()

print(languages)
