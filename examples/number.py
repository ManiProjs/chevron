from chevron import Number

age = Number(
    "How old are you?",
    integer=True,
    minimum=1,
).ask()

print(age)
