import os
import re

import pytest
from timeplus.env import Environment
WORKSPACE_LEN = 8
APIKEY_LEN = 60


def test_apikey_with_valid_key(test_environment):
    env = test_environment
    if os.environ.get("TIMEPLUS_API_KEY") is not None:
        assert env._configuration.api_key["X-Api-Key"] == os.environ.get("TIMEPLUS_API_KEY")


def test_apikey_with_invalid_key():
    if os.environ.get("TIMEPLUS_API_KEY") is not None:
        env = Environment()
        with pytest.raises(ValueError, match=f"The apikey should be {APIKEY_LEN} characters"):
            env.apikey("invalid_key")


def test_workspace_with_valid_name(test_environment):
    env = test_environment
    assert env._workspace == os.environ.get("TIMEPLUS_WORKSPACE")
