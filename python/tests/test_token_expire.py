import os
import time
import pytest
from timeplus import Env, Query


@pytest.mark.skip(reason="skip to avoid to generate too many tokens")
def test_token_expire():
    env = Env()
    env.audience(os.environ.get("TIMEPLUS_AUDIENCE"))
    env.client_id(os.environ.get("TIMEPLUS_API_CLIENT_ID"))
    env.client_secret(os.environ.get("TIMEPLUS_API_CLIENT_SECRET"))

    token = env.request_token()
    env.logger().debug(f"the token is {token}")
    assert token is not None
    assert "access_token" in token

    env.token(token["access_token"])

    results = Query.list()
    env.logger().debug(f"the result is {results}")

    time.sleep(120)

    results = Query.list()
    env.logger().debug(f"the result is {results}")

    time.sleep(120)

    results = Query.list()
    env.logger().debug(f"the result is {results}")
