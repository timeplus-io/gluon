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
