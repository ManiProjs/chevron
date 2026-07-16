from chevron import Password

password = Password("GitHub token").ask()

print(f"Password length: {len(password)}")
