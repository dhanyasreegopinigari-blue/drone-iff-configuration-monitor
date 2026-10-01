from backend.device_manager import DeviceManager


def test_initial_state():

    manager = DeviceManager(simulation_mode=True)

    assert manager.get_status() == "READY"
    assert manager.is_configured() is False
    assert manager.is_connected() is False


def test_configure_device():

    manager = DeviceManager(simulation_mode=True)

    result = manager.configure_device(
        "1234",
        "4321"
    )

    assert result is True
    assert manager.is_configured() is True
    assert manager.get_status() == "CONFIGURED"


def test_connect_device():

    manager = DeviceManager(simulation_mode=True)

    manager.configure_device(
        "1234",
        "4321"
    )

    result = manager.connect_device()

    assert result is True
    assert manager.is_connected() is True
    assert manager.get_status() == "CONNECTED"


def test_connection_check():

    manager = DeviceManager(simulation_mode=True)

    manager.configure_device(
        "1234",
        "4321"
    )

    manager.connect_device()

    assert manager.check_connection() is True


def test_disconnect_device():

    manager = DeviceManager(simulation_mode=True)

    manager.configure_device(
        "1234",
        "4321"
    )

    manager.connect_device()

    result = manager.disconnect_device()

    assert result is True
    assert manager.is_connected() is False
    assert manager.get_status() == "DISCONNECTED"


def test_connection_loss_simulation():

    manager = DeviceManager(simulation_mode=True)

    manager.configure_device(
        "1234",
        "4321"
    )

    manager.connect_device()

    manager.simulate_connection_loss()

    assert manager.is_connected() is False
    assert manager.get_status() == "DISCONNECTED"


def test_connection_recovery_simulation():

    manager = DeviceManager(simulation_mode=True)

    manager.configure_device(
        "1234",
        "4321"
    )

    manager.connect_device()

    manager.simulate_connection_loss()

    assert manager.is_connected() is False

    result = manager.simulate_connection_recovery()

    assert result is True
    assert manager.is_connected() is True
    assert manager.get_status() == "CONNECTED"