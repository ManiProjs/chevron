from chevron import Input


def validate_username(value: str):
    if len(value) < 3:
        return "Username must be at least 3 characters."

    if " " in value:
        return "Username cannot contain spaces."

    return True


username = Input(
    "Username",
    required=True,
    transform=str.lower,
    validator=validate_username,
).ask()

print(f"Hello, {username}!")
