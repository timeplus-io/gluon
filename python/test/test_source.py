import pytest
from timeplus import Source, Stream


def test_source_generator(test_environment):
    stream_name = "iot"
    source_name = "iot"
    # create a new stream
    stream = Stream(env=test_environment).name(stream_name)

    try:
        stream.delete()
    except Exception:
        pass

    stream = (
        Stream(env=test_environment)
        .name(stream_name)
        .column("device", "string")
        .column("number", "float32")
        .column("time", "string")
        .create()
    )

    source_type = "stream_generator"
    source_stream = "iot"
    source_properties = {"template": "iot"}
    source_description = ""
    source = (
        Source(env=test_environment)
        .name(source_name)
        .type(source_type)
        .stream(source_stream)
        .properties(source_properties)
        .description(source_description)
        .create()
    )

    source_list = Source(env=test_environment).list()
    source_id = source.id()
    assert source_name in [q.name for q in source_list]

    assert Source(env=test_environment).id(source_id).exist()

    source.delete()
    stream.delete()

    source_list = Source(env=test_environment).list()
    assert source_name not in [s.name for s in source_list]

    assert not Source(env=test_environment).id(source_id).exist()


@pytest.mark.skipif(reason="Skipping this test due to kafka source move to external stream")
def test_source_kafka(test_environment):
    stream_name = "test_kafka"
    source_name = "test_kafka"
    # create a new stream
    stream = Stream(env=test_environment).name(stream_name)

    try:
        stream.delete()
    except Exception:
        pass

    stream = (
        Stream(env=test_environment)
        .name(stream_name)
        .column("raw", "string")
        .create()
    )

    source_type = "kafka"
    source_stream = "test_kafka"
    source_properties = {
        "data_type": "text",
        "offset": "latest",
        "sasl": "none",
        "username": "",
        "password": "",
        "auto_field_extraction": True,
        "schema_registry_address": "",
        "schema_registry_api_key": "",
        "schema_registry_api_secret": "",
        "protobuf_message": "",
        "protobuf_schema": "",
        "group": "",
        "brokers": "kafka.user-gang:9092",
        "topic": "car_live_data",
        "tls": {
            "disable": True,
            "skip_verify_server": True
        }
    }
    source_description = ""
    source = (
        Source(env=test_environment)
        .name(source_name)
        .type(source_type)
        .stream(source_stream)
        .properties(source_properties)
        .description(source_description)
        .create()
    )

    source_list = Source(env=test_environment).list()
    source_id = source.id()
    assert source_name in [q.name for q in source_list]

    assert Source(env=test_environment).id(source_id).exist()

    source.delete()
    stream.delete()

    source_list = Source(env=test_environment).list()
    assert source_name not in [s.name for s in source_list]

    assert not Source(env=test_environment).id(source_id).exist()
