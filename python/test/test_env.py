import os
import re

import pytest
from timeplus.env import Environment
WORKSPACE_LEN = 8
APIKEY_LEN = 60


def test_apikey_with_valid_key(test_environment):
    env = test_environment
    assert env._configuration.api_key["X-Api-Key"] == os.environ.get("TIMEPLUS_API_KEY")


def test_apikey_with_invalid_key():
    env = Environment()
    with pytest.raises(ValueError, match=f"The apikey should be {APIKEY_LEN} characters"):
        env.apikey("invalid_key")


def test_workspace_with_valid_name(test_environment):
    env = test_environment
    assert env._workspace == os.environ.get("TIMEPLUS_WORKSPACE")


# def test_workspace_with_invalid_name():
#     env = Environment()
#     expected_error = f"Did you set the workspace name? Please set the workspace ID (usually {WORKSPACE_LEN} characters long)"
#     with pytest.raises(ValueError, match=re.escape(expected_error)):
#         env.workspace("invalid_workspace")


def test_address():
    env = Environment()
    url = "https://us.timeplus.cloud/"
    expected_host = "https://us.timeplus.cloud/api"

    env.address(url)

    assert env._address == "https://us.timeplus.cloud"
    assert env._configuration.host == expected_host
