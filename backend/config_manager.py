import json
from pathlib import Path


class ConfigManager:

    def __init__(self, config_file="config.json"):
        self.config_file = Path(config_file)

    def save_configuration(self, device_id, ass):

        configuration = {
            "device_id": device_id,
            "ass": ass
        }

        try:

            with open(
                self.config_file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    configuration,
                    file,
                    indent=4
                )

            return configuration

        except OSError as error:

            print("Error saving configuration:", error)

            return None

    def load_configuration(self):

        if not self.config_file.exists():
            return None

        try:

            with open(
                self.config_file,
                "r",
                encoding="utf-8"
            ) as file:

                configuration = json.load(file)

            return configuration

        except json.JSONDecodeError as error:

            print("Invalid configuration file:", error)

            return None

        except OSError as error:

            print("Error loading configuration:", error)

            return None

    def reset_configuration(self):

        if not self.config_file.exists():
            return True

        try:

            self.config_file.unlink()

            return True

        except OSError as error:

            print("Error resetting configuration:", error)

            return False