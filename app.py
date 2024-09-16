from window import Window
from update import Update
import subprocess


def run():
    subprocess.run(['git', 'fetch'])

    local_commit = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    remote_commit = subprocess.run(['git', 'rev-parse', 'origin/main'], capture_output=True, text=True).stdout.strip()

    if (local_commit == remote_commit):
        root = Window()
        root.run()
    else:
        updater = Update()
        updater.run()


if __name__ == "__main__":
    run()
