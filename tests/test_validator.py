from backend.validator import ConfigValidator


def test_valid_configuration():

    valid, message = ConfigValidator.validate_configuration(
        "1234",
        "4321"
    )

    assert valid is True
    assert message == "Configuration is valid."


def test_missing_device_id():

    valid, message = ConfigValidator.validate_configuration(
        "",
        "4321"
    )

    assert valid is False


def test_missing_ass():

    valid, message = ConfigValidator.validate_configuration(
        "1234",
        ""
    )

    assert valid is False


def test_invalid_device_id():

    valid, message = ConfigValidator.validate_configuration(
        "123",
        "4321"
    )

    assert valid is False


def test_invalid_ass():

    valid, message = ConfigValidator.validate_configuration(
        "1234",
        "abc"
    )

    assert valid is False