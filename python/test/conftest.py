"""
conftest.py
"""

import pytest
import os
import random

from timeplus import Environment
from timeplus import Stream
from timeplus.error import TimeplusAPIError


@pytest.fixture
def test_environment():
    api_key = os.environ.get("TIMEPLUS_API_KEY")
    api_address = os.environ.get("TIMEPLUS_HOST")
    worksapce = os.environ.get("TIMEPLUS_WORKSPACE")

    return Environment().address(api_address).apikey(api_key).workspace(worksapce)


@pytest.fixture
def test_stream(test_environment):
    stream_name = "test_stream"

    # Create a new stream instance with the given name
    stream = Stream(env=test_environment).name(stream_name)

    try:
        stream.delete()
    except Exception:
        pass

    # Create a new stream
    stream = (
        Stream(env=test_environment)
        .name(stream_name)
        .column("time", "integer")
        .column("data", "string")
        .create()
    )

    value = [["time", "data"], [[0, "abcd"]]]
    stream.ingest(*value)
    # Provide the stream to the test
    return stream



