from timeplus import Env


def test_env():
    env1 = Env.getInstance()
    env2 = Env.getInstance()

    assert env1 is env2

    env1.login()

    assert env1 is Env.getInstance()
    assert Env.getInstance().token()["access_token"] is not None
    assert env1.token()["access_token"] is not None
    assert env2.token()["access_token"] is not None
