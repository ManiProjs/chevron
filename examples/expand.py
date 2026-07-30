from chevron import Expand


def main():
    action = Expand(
        "Choose an action",
        {
            "n": "Create a new file",
            "o": "Open a file",
            "d": "Delete a file",
            "q": "Quit",
        },
    ).ask()

    print(f"You selected: {action}")


if __name__ == "__main__":
    main()
