import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer

from backend.config_manager import ConfigManager
from backend.validator import ConfigValidator
from backend.device_manager import DeviceManager
from backend.logger import AppLogger

class DroneIFF(QMainWindow):

    def __init__(self):
        super().__init__()

        # Load the interface created in Qt Designer
        uic.loadUi("main.ui", self)

        # Configuration file
        self.config_manager = ConfigManager()

        # Device manager
        self.device_manager = DeviceManager(
            simulation_mode=True
        )

        self.logger = AppLogger("device.log")

        self.logger.info("Application started")

        self.last_connection_state = None

        self.monitor_timer = QTimer()

        self.monitor_timer.timeout.connect(
            self.monitor_device
        )

        self.last_connection_state = None

        self.monitor_timer = QTimer()
        self.monitor_timer.timeout.connect(self.monitor_device)
        self.monitor_timer.start(2000)

        # ComboBox signals
        self.deviceIDCombo.currentTextChanged.connect(
            self.device_id_changed
        )

        self.assCombo.currentTextChanged.connect(
            self.ass_changed
        )

        # Save button
        self.saveButton.clicked.connect(
            self.save_configuration
        )

        # Reset button
        self.resetButton.clicked.connect(
            self.reset_configuration
        )

        # Apply button
        self.applyButton.clicked.connect(
            self.apply_configuration
        )

        # Load saved configuration
        self.load_configuration()

        # Initial status
        self.update_status("READY")

    def device_id_changed(self, value):
        print("Device ID selected:", value)

    def ass_changed(self, value):
        print("ASS selected:", value) 

    def update_status(self, status):

        if status == "READY":

            self.statusValueLabel.setText("🟢 READY")
            self.deviceReadyLabel.setText("● Device Ready")

        elif status == "CONFIGURED":

            self.statusValueLabel.setText("🟢 CONFIGURED")
            self.deviceReadyLabel.setText("● Configuration Ready")

        elif status == "ERROR":

            self.statusValueLabel.setText("🔴 ERROR")
            self.deviceReadyLabel.setText("● Configuration Error")

        elif status == "SAVED":

            self.statusValueLabel.setText("🟢 SAVED")
            self.deviceReadyLabel.setText("● Configuration Saved")

        elif status == "CONNECTED":

            self.statusValueLabel.setText("🟢 CONNECTED")
            self.deviceReadyLabel.setText("● Device Connected")

        elif status == "DISCONNECTED":

            self.statusValueLabel.setText("🟡 DISCONNECTED")
            self.deviceReadyLabel.setText("● Device Disconnected")     

    def reset_configuration(self):

        try:

            success = self.config_manager.reset_configuration()

            if not success:

                self.logger.error(
                    "Configuration reset failed"
                )

                QMessageBox.critical(
                    self,
                    "Reset Error",
                    "Unable to reset the saved configuration."
                )

                return

            self.deviceIDCombo.setCurrentIndex(0)
            self.assCombo.setCurrentIndex(0)

            self.device_manager.disconnect_device()

            self.update_status("READY")

            self.logger.info(
                "Configuration reset successfully"
            )

            print("Configuration reset.")

            QMessageBox.information(
                self,
                "Reset",
                "Configuration has been reset."
            )

        except Exception as error:

            self.logger.error(
                f"Unexpected reset error: {error}"
            )

            QMessageBox.critical(
                self,
                "Unexpected Error",
                "An unexpected error occurred while resetting."
            )
   
    def apply_configuration(self):

        device_id = self.deviceIDCombo.currentText().strip()
        ass = self.assCombo.currentText().strip()

        print("Applying configuration...")
        print("Device ID:", device_id)
        print("ASS:", ass)

        # Validate configuration
        valid, message = ConfigValidator.validate_configuration(
            device_id,
            ass
        )

        if not valid:

            self.update_status("ERROR")

            self.logger.warning(
                f"Configuration rejected: {message}"
            )

            QMessageBox.warning(
                self,
                "Invalid Configuration",
                message
            )

            print("Configuration rejected:", message)

            return

        try:

            # Configure device
            configured = self.device_manager.configure_device(
                device_id,
                ass
            )

            if not configured:

                self.update_status("ERROR")

                self.logger.error(
                    "Device configuration failed"
                )

                QMessageBox.critical(
                    self,
                    "Configuration Error",
                    "The device configuration could not be applied."
                )

                return

            self.logger.info(
                f"Device configured - ID: {device_id}, ASS: {ass}"
            )

            # Connect device
            connected = self.device_manager.connect_device()

            if connected:

                self.logger.info(
                    "Device connected successfully"
                )

                self.update_status("CONNECTED")

                print("Configuration accepted.")
                print("Device connected.")

                QMessageBox.information(
                    self,
                    "Configuration Applied",
                    f"Configuration applied successfully.\n\n"
                    f"Device ID: {device_id}\n"
                    f"ASS: {ass}"
                )

            else:

                self.logger.warning(
                    "Device connection failed"
                )

                self.update_status("CONFIGURED")

                QMessageBox.warning(
                    self,
                    "Connection Failed",
                    "Configuration was applied, but the device "
                    "could not be connected."
                )

        except Exception as error:

            self.update_status("ERROR")

            self.logger.error(
                f"Unexpected Apply error: {error}"
            )

            print(
                "Unexpected error during Apply:",
                error
            )

            QMessageBox.critical(
                self,
                "Unexpected Error",
                "An unexpected error occurred while applying "
                "the configuration."
            )
        
    def save_configuration(self):

        device_id = self.deviceIDCombo.currentText()
        ass = self.assCombo.currentText()

        valid, message = ConfigValidator.validate_configuration(
            device_id,
            ass
       )

        if not valid:

            QMessageBox.warning(
                self,
                "Invalid Configuration",
                message
           )

            self.logger.warning(
                f"Invalid configuration: {message}"
            )

            return

        try:

            configuration = self.config_manager.save_configuration(
                device_id,
                ass
            )

            if configuration is None:

                QMessageBox.critical(
                    self,
                    "Save Error",
                    "Unable to save configuration."
                )

                self.logger.error(
                    "Configuration save failed"
                )

                return

            self.update_status("SAVED")

            self.logger.info(
                f"Configuration saved: Device ID={device_id}, ASS={ass}"
            )

            print(
                "Configuration saved:",
                configuration
            )

        except Exception as error:

            QMessageBox.critical(
                self,
                "Unexpected Error",
                "An unexpected error occurred while saving configuration."
            )

            self.logger.error(
                f"Unexpected save error: {error}"
            )
        
    def load_configuration(self):

        try:

            configuration = self.config_manager.load_configuration()

            if configuration is None:
                print("No saved configuration found.")
                return

            device_id = configuration.get("device_id")
            ass = configuration.get("ass")

            if device_id:

                index = self.deviceIDCombo.findText(device_id)

                if index >= 0:
                    self.deviceIDCombo.setCurrentIndex(index)

            if ass:

                index = self.assCombo.findText(ass)

                if index >= 0:
                    self.assCombo.setCurrentIndex(index)

            print("Configuration loaded:", configuration)

        except Exception as error:

            print("Error while loading:", error)
            self.update_status("ERROR")

    def monitor_device(self):

        if not self.device_manager.is_configured():
            return

        connected = self.device_manager.check_connection()

        current_state = self.device_manager.get_status()

        print(
            "Device monitor check:",
            current_state
        )

        if connected:

            self.update_status("CONNECTED")

            if self.last_connection_state != "CONNECTED":

                self.logger.info("Device connection established")

                self.last_connection_state = "CONNECTED"

        else:

            self.update_status("DISCONNECTED")

            if self.last_connection_state != "DISCONNECTED":

                self.logger.warning("Device connection lost")

                self.last_connection_state = "DISCONNECTED"   

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DroneIFF()
    window.show()

    sys.exit(app.exec_())