from timeplus import Env


def test_env():
    env1 = Env()
    env2 = Env()
    env1.login()

    assert env1.access_token() is not None
    assert env2.access_token() is ""
