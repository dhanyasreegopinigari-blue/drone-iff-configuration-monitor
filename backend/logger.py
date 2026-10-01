from datetime import datetime
from pathlib import Path


class AppLogger:

    def __init__(self, log_file="device.log"):

        self.log_file = Path(log_file)

    def log(self, message):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        log_entry = f"[{timestamp}] {message}\n"

        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(log_entry)

    def info(self, message):

        self.log(f"INFO: {message}")

    def warning(self, message):

        self.log(f"WARNING: {message}")

    def error(self, message):

        self.log(f"ERROR: {message}")