from backend.simulator import Simulator


class DeviceManager:

    STATES = {
        "INITIALIZING": "INITIALIZING",
        "READY": "READY",
        "CONFIGURING": "CONFIGURING",
        "CONFIGURED": "CONFIGURED",
        "CONNECTING": "CONNECTING",
        "CONNECTED": "CONNECTED",
        "DISCONNECTED": "DISCONNECTED",
        "ERROR": "ERROR"
    }

    def __init__(self, simulation_mode=True):

        self.simulation_mode = simulation_mode

        self.device_id = None
        self.ass = None

        self.state = self.STATES["INITIALIZING"]

        self.configured = False
        self.connected = False

        # Create the simulated device
        if self.simulation_mode:
            self.device = Simulator()
        else:
            self.device = None

        self.state = self.STATES["READY"]

    def configure_device(self, device_id, ass):

        self.state = self.STATES["CONFIGURING"]

        self.device_id = device_id
        self.ass = ass

        if self.device is not None:

            success = self.device.configure(
                device_id,
                ass
            )

            if not success:

                self.state = self.STATES["ERROR"]

                return False

        self.configured = True
        self.state = self.STATES["CONFIGURED"]

        print("Device configured.")
        print("Device ID:", self.device_id)
        print("ASS:", self.ass)

        return True

    def connect_device(self):

        if not self.configured:

            self.state = self.STATES["ERROR"]

            print("Device cannot connect.")
            print("Configuration is missing.")

            return False

        self.state = self.STATES["CONNECTING"]

        if self.device is not None:

            success = self.device.connect()

            if success:

                self.connected = True
                self.state = self.STATES["CONNECTED"]

                return True

        self.state = self.STATES["ERROR"]

        return False

    def disconnect_device(self):

        if self.device is not None:

            self.device.disconnect()

        self.connected = False
        self.state = self.STATES["DISCONNECTED"]

        print("Device disconnected.")

        return True

    def check_connection(self):

        if self.device is not None:

            self.connected = self.device.is_connected()

            return self.connected

        return False

    def get_status(self):

        return self.state

    def is_connected(self):

        return self.connected

    def is_configured(self):

        return self.configured

    def is_simulation_mode(self):

        return self.simulation_mode

    def simulate_connection_loss(self):

        if self.device is not None:

            self.device.simulate_connection_loss()

            self.connected = False
            self.state = self.STATES["DISCONNECTED"]

            print("Device connection loss simulated.")

    def simulate_connection_recovery(self):

        if self.device is not None:

            self.device.simulate_connection_recovery()

            self.connected = True
            self.state = self.STATES["CONNECTED"]

            print("Device connection recovery simulated.")

            return True
        return False