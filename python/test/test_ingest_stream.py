import json
import time

import pytest
from timeplus import Stream, Query
import datetime


def test_ingest(test_environment, test_stream):
    data = [["time", "data"], [[1, "efgh"]]]
    try:
        test_stream.ingest(*data)
    except Exception as e:
        pytest.fail(f"Ingest method failed with exception {e}")

    time.sleep(3)

    query = (
        Query(env=test_environment)
        .sql(query="SELECT * FROM table(test_stream)")
        .create()
    )

    results = []
    for event in query.result():
        if event.event == "message":
            results.extend(json.loads(event.data))
    print(results)
    print(results[1][1])

    assert len(results) > 1, "No data returned from the stream"
    assert results[1][0] == 1, "Returned time does not match the ingested integer"
    assert results[1][1] == 'efgh', "Returned data does not match the ingested string"

    query.delete()


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

    time.sleep(3)

    query = (
        Query(env=test_environment)
        .sql(query="SELECT * FROM table(test_stream)")
        .create()
    )
    results = []
    for event in query.result():
        if event.event == "message":
            results.extend(json.loads(event.data))
    print(results)
    print(results[0][0])

    assert len(results) > 1, "No data returned from the stream"
    assert results[0][0] == '{"time":1,"data":"abcd"}', "Returned data does not match the ingested data"
    assert results[1][0] == '{"time":2,"data":"xyz"}', "Returned data does not match the ingested data"

    query.delete()


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

    time.sleep(3)

    query = (
        Query(env=test_environment)
        .sql(query="SELECT * FROM table(test_stream)")
        .create()
    )
    results = []
    for event in query.result():
        if event.event == "message":
            results.extend(json.loads(event.data))
    print(results)
    print(results[0][0])

    assert results is not None, "No data returned from the stream"
    assert results[0][0] == payload, "Returned data does not match the ingested data"

    query.delete()


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

    time.sleep(3)

    query = (
        Query(env=test_environment)
        .sql(query="SELECT * FROM table(test_stream)")
        .create()
    )
    results = []
    for event in query.result():
        if event.event == "message":
            results.extend(json.loads(event.data))
    print(results)
    print(results[0][0])
    print(results[0])

    assert len(results) > 1, "No data returned from the stream"
    assert results[1][0] == 2, "Returned data does not match the ingested data"
    assert results[1][1] == 'hello', "Returned data does not match the ingested data"
    assert results[2][0] == 1, "Returned data does not match the ingested data"
    assert results[2][1] == 'world', "Returned data does not match the ingested data"

    query.delete()
