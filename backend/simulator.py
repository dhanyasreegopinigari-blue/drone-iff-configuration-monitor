from backend.device_interface import DeviceInterface


class Simulator(DeviceInterface):

    def __init__(self):

        self.device_id = None
        self.ass = None
        self.connected = False

    def configure(self, device_id, ass):

        self.device_id = device_id
        self.ass = ass

        print("Simulator configured.")
        print("Device ID:", self.device_id)
        print("ASS:", self.ass)

        return True

    def connect(self):

        print("Simulator connecting...")

        self.connected = True

        print("Simulator connected.")

        return True

    def disconnect(self):

        print("Simulator disconnecting...")

        self.connected = False

        print("Simulator disconnected.")

        return True

    def is_connected(self):

        return self.connected

    def simulate_connection_loss(self):

        print("SIMULATION: Connection loss triggered.")

        self.connected = False

    def simulate_connection_recovery(self):

        print("SIMULATION: Connection recovery triggered.")

        self.connected = True