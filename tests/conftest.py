import os
from collections.abc import Iterator
from enum import StrEnum

import pytest


class EnvTest(StrEnum):
    DB_HOST = ""
    DB_PORT = "null"
    DB_USER = ""
    DB_PASSWORD = ""
    DB_NAME = ""
    DB_SCHEME = "sqlite"


@pytest.fixture(autouse=True, scope="session")
def set_env_vars() -> Iterator[None]:
    for var in EnvTest:
        os.environ[var.name] = var.value

    yield

    for var in EnvTest:
        del os.environ[var.name]
