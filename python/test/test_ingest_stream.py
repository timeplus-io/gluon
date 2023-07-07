import json

import pytest
from timeplus import Stream, Query
import datetime


def test_ingest(test_environment, test_stream):
    data = [["time", "data"], [[1, "efgh"]]]
    try:
        test_stream.ingest(*data)
    except Exception as e:
        pytest.fail(f"Ingest method failed with exception {e}")

    test_stream.delete()


def test_stream_ingest_lines(test_environment,test_stream):
    test_stream.delete()

    stream = (
        Stream(env=test_environment)
        .name("test_stream")
        .column("raw", "string")
        .create()
    )
    payload = '{"time":1,"data":"abcd"}\n{"time":2,"data":"xyz"}'

    # Ingest data in 'lines' format
    try:
        stream.ingest(payload=payload, format="lines")
    except Exception as e:
        pytest.fail(f"Ingest lines method failed with exception {e}")

    stream.delete()


def test_stream_ingest_raw(test_environment,test_stream):
    test_stream.delete()

    payload = """
    {"a":1,"b":"world"}
    {"a":2,"b":"hello"}
    """

    stream = (
        Stream(env=test_environment)
        .name("test_stream")
        .column("raw", "string")
        .create()
    )

    # Ingest data in 'raw' format
    try:
        stream.ingest(payload=payload, format="raw")
    except Exception as e:
        pytest.fail(f"Ingest raw method failed with exception {e}")

    stream.delete()


def test_json_ingest(test_environment, test_stream):
    payload = """
    {"time":2,"data":"hello"}
    {"time":1,"data":"world"}
    """

    # Ingest data in 'streaming' format
    try:
        test_stream.ingest(payload=payload, format="streaming")
    except Exception as e:
        pytest.fail(f"Ingest streaming method failed with exception {e}")

    # Clean up: delete the created stream
    test_stream.delete()
