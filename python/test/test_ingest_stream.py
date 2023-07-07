import json

from timeplus import Stream, Query
import datetime


def test_ingest(test_environment):
    name = "test_ingest_stream"
    data = ["time", "data"]
    values = [[datetime.datetime.now(), "abcd"]]

    stream = (
        Stream(env=test_environment)
        .name(name)
        .column("time", "datetime64(3)")
        .column("data", "string")
        .create()
    )

    stream.ingest(data, values)

    query_result = Query(env=test_environment).sql(f"select * from {name}").execute().fetchall()

    assert len(query_result) == 1
    assert query_result[0].time == values[0][0]
    assert query_result[0].data == values[0][1]

    stream.delete()


def test_stream_ingest_lines(test_environment):
    stream_name = "test_ingest_lines"
    payload = '{"a":1,"b":"world"}\n{"a":2,"b":"hello"}'

    stream = (
        Stream(env=test_environment)
        .name(stream_name)
        .column("raw", "string")
        .create()
    )
    # Ingest data in 'lines' format
    stream.ingest(payload=payload, format="lines")
    query_result = Query(env=test_environment).sql(f"select raw from {stream_name}").execute().fetchall()

    # Check that the result is as expected
    assert len(query_result) == 2
    assert query_result[0]['raw'] == '{"a":1,"b":"world"}'
    assert query_result[1]['raw'] == '{"a":2,"b":"hello"}'

    # Clean up: delete the created stream
    stream.delete()


def test_stream_ingest_raw(test_environment):
    stream_name = "test_ingest_raw"
    payload = """
    {"a":1,"b":"world"}
    {"a":2,"b":"hello"}
    """

    stream = (
        Stream(env=test_environment)
        .name(stream_name)
        .column("raw", "string")
        .create()
    )

    # Ingest data in 'raw' format
    stream.ingest(payload=payload, format="raw")
    query_result = Query(env=test_environment).sql(f"select raw from {stream_name}").execute().fetchall()

    # Check that the result is as expected
    assert len(query_result) == 1
    assert query_result[0]['raw'] == payload.strip()

    # Clean up: delete the created stream
    stream.delete()


def test_json_ingest(test_environment):
    stream_name = "test_ingest_json"
    payload = """
    {"a":2,"b":"hello"}
    {"a":1,"b":"world"}
    """
    payload_json = [json.loads(line) for line in payload.strip().split("\n")]

    stream = (
        Stream(env=test_environment)
        .name(stream_name)
        .column("a", "integer")
        .column("b", "string")
        .create()
    )

    # Ingest data in 'streaming' format
    stream.ingest(payload=payload, format="streaming")
    query_result = Query(env=test_environment).sql(f"select * from {stream_name}").execute().fetchall()

    # Check that the result is as expected
    assert len(query_result) == 2
    assert (query_result[0]['a'], query_result[0]['b']) in [(item['a'], item['b']) for item in payload_json]
    assert (query_result[1]['a'], query_result[1]['b']) in [(item['a'], item['b']) for item in payload_json]

    # Clean up: delete the created stream
    stream.delete()
