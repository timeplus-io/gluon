"""
conftest.py
"""
import pytest
import os

from timeplus import Env


def staging_environment():
    token = os.environ.get("TIMEPLUS_API_TOKEN")
    env = (
        Env().schema("https").host("staging.demo.timeplus.io").port("443").token(token)
    )
    # set current environment when you have more than 1 environment
    Env.setCurrent(env)
    return env


def demo_environment():
    token = os.environ.get("TIMEPLUS_API_TOKEN")
    env = Env().schema("https").host("demo.timeplus.com").port("443").token(token)
    Env.setCurrent(env)
    return env


def latest_environment():
    token = os.environ.get("TIMEPLUS_API_TOKEN")
    env = Env().schema("https").host("latest.timeplus.io").port("443").token(token)
    Env.setCurrent(env)
    return env


def playground_environment():
    env = Env().schema("https").host("play.timeplus.com").port("443")
    Env.setCurrent(env)
    return env


def local_environment():
    token = os.environ.get("TIMEPLUS_API_TOKEN")
    env = Env().token(token)
    Env.setCurrent(env)
    return env


@pytest.fixture
def test_environment():
    env_name = os.environ.get("TIMEPLUS_ENVIRONMENT")
    if env_name == "staging":
        return staging_environment()

    if env_name == "demo":
        return demo_environment()

    if env_name == "latest":
        return latest_environment()

    return local_environment()


@pytest.fixture
def confluent_broker():
    return "pkc-ld537.ca-central-1.aws.confluent.cloud:9092"


@pytest.fixture
def demo_broker():
    return "54.241.124.151:9092"
