class DashTestingError(Exception):
    """Base error for pytest-dash."""


class InvalidDriverError(DashTestingError):
    """An invalid selenium driver was specified."""


class NoAppFoundError(DashTestingError):
    """No `app` was found in the file."""


class DashAppLoadingError(DashTestingError):
    """The dash app failed to load"""


class ServerCloseError(DashTestingError):
    """The server cannot be closed"""


class TestingTimeoutError(DashTestingError):
    """"all timeout error about dash testing"""
