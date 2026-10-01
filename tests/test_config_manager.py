from backend.config_manager import ConfigManager


def test_save_configuration(tmp_path):

    config_file = tmp_path / "test_config.json"

    manager = ConfigManager(config_file)

    configuration = manager.save_configuration(
        "1234",
        "4321"
    )

    assert configuration == {
        "device_id": "1234",
        "ass": "4321"
    }

    assert config_file.exists()


def test_load_configuration(tmp_path):

    config_file = tmp_path / "test_config.json"

    manager = ConfigManager(config_file)

    manager.save_configuration(
        "1234",
        "4321"
    )

    configuration = manager.load_configuration()

    assert configuration == {
        "device_id": "1234",
        "ass": "4321"
    }


def test_load_when_configuration_does_not_exist(tmp_path):

    config_file = tmp_path / "missing_config.json"

    manager = ConfigManager(config_file)

    configuration = manager.load_configuration()

    assert configuration is None


def test_reset_configuration(tmp_path):

    config_file = tmp_path / "test_config.json"

    manager = ConfigManager(config_file)

    manager.save_configuration(
        "1234",
        "4321"
    )

    assert config_file.exists()

    result = manager.reset_configuration()

    assert result is True
    assert not config_file.exists()