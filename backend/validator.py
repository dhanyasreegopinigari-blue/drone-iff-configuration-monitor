class ConfigValidator:

    @staticmethod
    def validate_configuration(device_id, ass):

        if not device_id:
            return False, "Device ID is not selected."

        if not ass:
            return False, "ASS is not selected."

        if not device_id.isdigit():
            return False, "Device ID must contain only numbers."

        if not ass.isdigit():
            return False, "ASS must contain only numbers."

        if len(device_id) != 4:
            return False, "Device ID must contain exactly 4 digits."

        if len(ass) != 4:
            return False, "ASS must contain exactly 4 digits."

        return True, "Configuration is valid."