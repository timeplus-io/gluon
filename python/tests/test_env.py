import os
from timeplus import Env


def test_env():
    env1 = Env()
    env2 = Env()

    Env.setCurrent(env2)
    assert Env.current() is env2

    assert env1.token() is not None
    assert env2.token() == ""


def test_stage_env(staging_environment):
    assert staging_environment.info() is not None
    assert staging_environment.ping() is not None


def test_request_token():
    env = Env()
    env.audience(os.environ.get("TIMEPLUS_AUDIENCE"))
    env.client_id(os.environ.get("TIMEPLUS_API_CLIENT_ID"))
    env.client_secret(os.environ.get("TIMEPLUS_API_CLIENT_SECRET"))

    token = env.request_token()
    assert token is not None
    assert "access_token" in token
