"""
conftest.py
"""
import pytest
import os

from timeplus import Env


@pytest.fixture
def staging_environment():
    client_id = os.environ.get("AUTH0_API_CLIENT_ID")
    client_secret = os.environ.get("AUTH0_API_CLIENT_SECRET")
    env = (
        Env()
        .schema("https")
        .host("kafka1.dev.timeplus.io")
        .port("443")
        .login(client_id=client_id, client_secret=client_secret)
    )
    Env.setCurrent(env)  # set current environment when you have more than 1 environment
    return env


@pytest.fixture
def local_environment():
    env = Env()
    Env.setCurrent(env)
    return env