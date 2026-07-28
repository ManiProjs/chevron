import time

from chevron import Spinner


spinner = Spinner("Installing dependencies...")

spinner.start()

try:
    time.sleep(3)
finally:
    spinner.stop()

print("Done!")
