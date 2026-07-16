from chevron import (
    Checkbox,
    Choice,
    Confirm,
    Input,
    Number,
    Password,
    Select,
    Editor,
)

print("=== Chevron Demo ===")

name = Input("Name").ask()

password = Password("Password").ask()

age = Number(
    "Age",
    integer=True,
).ask()

language = Select(
    "Favorite language",
    [
        Choice("Python"),
        Choice("Rust", value="rs", description="Fast and safe systems language"),
        Choice("Go", value="go"),
        Choice("Zig", value="zig"),
    ],
).ask()

skills = Checkbox(
    "Languages you know",
    [
        Choice("Python"),
        Choice("Rust"),
        Choice("Go"),
        Choice("Zig"),
    ],
).ask()

description = Editor(
    "Project description",
    file_extension=".md",
).ask()

remember = Confirm(
    "Remember your choices?",
).ask()

print()

print(f"Name        : {name}")
print(f"Password    : {'*' * len(password)}")
print(f"Age         : {age}")
print(f"Language    : {language}")
print(f"Skills      : {skills}")
print(f"Description : {description}")
print(f"Remember?   : {remember}")
