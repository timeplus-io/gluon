from timeplus import Env


def test_env():
    env = Env()
    env.login()
    assert env.token()["access_token"] is not None
