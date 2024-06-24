import json
import time
import os
import pytest

from timeplus import Stream, Query
import datetime

time_wait = 5


def test_ingest(test_environment, test_stream):
    # there is 4 row data in test stream already
    time.sleep(time_wait)
    # wait previous data ingested
    data = [["time", "data"], [[1, "efgh"]]]
    try:
        test_stream.ingest(*data)
    except Exception as e:
        pytest.fail(f"Ingest method failed with exception {e}")

    time.sleep(time_wait)

    query = (
        Query(env=test_environment)
        .sql(query="SELECT * FROM table(test_stream)")
        .create()
    )

    results = []
    for event in query.result():
        if event.event == "message":
            results.extend(json.loads(event.data))

    result_length = len(results)
    assert len(results) > 1, "No data returned from the stream"
    assert results[result_length-1][0] == 1, "Returned time does not match the ingested integer"
    assert results[result_length-1][1] == 'efgh', "Returned data does not match the ingested string"

    query.delete()


def test_stream_ingest_lines(test_environment, test_stream_raw):

    payload = '{"time":1,"data":"abcd"}\n{"time":2,"data":"xyz"}'

    # Ingest data in 'lines' format
    try:
        test_stream_raw.ingest(payload=payload, format="lines")
    except Exception as e:
        pytest.fail(f"Ingest lines method failed with exception {e}")

    time.sleep(time_wait)

    query = (
        Query(env=test_environment)
        .sql(query="SELECT * FROM table(test_stream_raw)")
        .create()
    )
    results = []
    for event in query.result():
        if event.event == "message":
            results.extend(json.loads(event.data))

    result_length = len(results)

    assert len(results) > 1, "No data returned from the stream"
    assert results[result_length-2][0] == '{"time":1,"data":"abcd"}', "Returned data does not match the ingested data"
    assert results[result_length-1][0] == '{"time":2,"data":"xyz"}', "Returned data does not match the ingested data"

    query.delete()

def test_stream_ingest_raw(test_environment, test_stream_raw):
    payload = """
    {"a":1,"b":"world"}
    {"a":2,"b":"hello"}
    """

    # Ingest data in 'raw' format
    try:
        test_stream_raw.ingest(payload=payload, format="raw")
    except Exception as e:
        pytest.fail(f"Ingest raw method failed with exception {e}")

    time.sleep(time_wait)

    query = (
        Query(env=test_environment)
        .sql(query="SELECT * FROM table(test_stream_raw)")
        .create()
    )
    results = []
    for event in query.result():
        if event.event == "message":
            results.extend(json.loads(event.data))
    
    result_length = len(results)
    assert results is not None, "No data returned from the stream"
    assert results[result_length-1][0] == payload, "Returned data does not match the ingested data"

    query.delete()


def test_json_ingest(test_environment, test_stream):
    # there is 4 row data in test stream already
    time.sleep(time_wait)
    # wait previous data ingested
    payload = """
    {"time":2,"data":"hello"}
    {"time":1,"data":"world"}
    """

    # Ingest data in 'streaming' format
    try:
        test_stream.ingest(payload=payload, format="streaming")
    except Exception as e:
        pytest.fail(f"Ingest streaming method failed with exception {e}")

    time.sleep(time_wait)

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

    result_length = len(results)
    assert len(results) > 1, "No data returned from the stream"
    assert results[result_length-2][0] == 2, "Returned data does not match the ingested data"
    assert results[result_length-2][1] == 'hello', "Returned data does not match the ingested data"
    assert results[result_length-1][0] == 1, "Returned data does not match the ingested data"
    assert results[result_length-1][1] == 'world', "Returned data does not match the ingested data"

    query.delete()
