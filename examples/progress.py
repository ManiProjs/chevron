from time import sleep

from chevron import Progress


def basic():
    with Progress(
        total=100,
        description="Downloading",
    ) as progress:
        for _ in range(100):
            sleep(0.03)
            progress.advance()


def custom_steps():
    with Progress(
        total=50,
        description="Building",
    ) as progress:
        for _ in range(10):
            sleep(0.1)
            progress.advance(5)


def manual_update():
    progress = Progress(
        total=100,
        description="Installing",
    )

    progress.update(25)
    sleep(1)

    progress.update(75)
    sleep(1)

    progress.finish()


def main():
    print("Basic progress:")
    basic()

    print("\nCustom increments:")
    custom_steps()

    print("\nManual updates:")
    manual_update()


if __name__ == "__main__":
    main()
