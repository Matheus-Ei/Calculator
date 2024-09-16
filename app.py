from window import Window
from update import Update
import subprocess


def run():
    result = subprocess.run(['git', 'fetch'], capture_output=True, text=True)
    if (result.stdout == ""):
        pass
    else:
        updater = Update()
        updater.run()

    root = Window()
    root.run()


if __name__ == "__main__":
    run()
