"""
conftest.py
"""
import pytest
import os
import random

from timeplus import Environment
from timeplus import Stream


@pytest.fixture
def test_environment():
    api_key = os.environ.get("TIMEPLUS_API_KEY")
    api_address = os.environ.get("TIMEPLUS_HOST")
    worksapce = os.environ.get("TIMEPLUS_WORKSPACE")

    return Environment().address(api_address).apikey(api_key).workspace(worksapce)


@pytest.fixture
def test_table(test_environment):
    # Create a new stream
    stream_name = "test_stream"
    stream = (
        Stream(env=test_environment)
        .name(stream_name)
        .column("id", "integer")
        .column("data", "string")
        .create()
    )

    # Generate and ingest some random data
    data = ["id", "data"]
    values = [[i, f"random_string_{random.randint(0, 1000)}"] for i in range(10)]
    stream.ingest(data, values)

    # Provide the stream to the test
    yield stream

    # Clean up: delete the stream after test
    stream.delete()
