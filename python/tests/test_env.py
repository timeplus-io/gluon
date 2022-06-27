import os
import pytest
from timeplus import Env


def test_env():
    env1 = Env()
    env2 = Env()

    Env.setCurrent(env2)
    assert Env.current() is env2


def test_stage_env(test_environment):
    assert test_environment.info() is not None
    assert test_environment.ping() is not None
