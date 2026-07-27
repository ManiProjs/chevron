from chevron import Select, Theme


theme = Theme(
    pointer="➜",
    pointer_style="bold fg:#A78BFA",
    selected_style="bold fg:#A78BFA",
    footer_style="fg:#888888",
)


result = Select(
    "Choose a language",
    [
        "Python",
        "Rust",
        "Go",
    ],
    theme=theme,
).ask()


print(f"Selected: {result}")
