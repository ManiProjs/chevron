from chevron import Select

language = Select(
    "Favorite language",
    [
        "Python",
        "Rust",
        "Go",
        "Zig",
    ],
).ask()

print(language)
