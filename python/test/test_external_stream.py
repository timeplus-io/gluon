import os
from timeplus import ExternalStream


def test_external_stream(test_environment):
    name = "gluon_test_external_name"

    external_stream_password = os.environ.get("EXTERNAL_STREAM_PASSWORD")

    # Create a new stream instance with the given name
    stream = ExternalStream(env=test_environment).name(name)

    try:
        stream.delete()
    except Exception:
        pass

    # create a new stream
    # happy test, depending on the topic exist
    stream = (
        ExternalStream(env=test_environment)
        .name(name)
        .add_column("raw", "string")
        .add_settings("type", "kafka")
        .add_settings("brokers", "kafka-public-read-timeplus.a.aivencloud.com:28864")
        .add_settings("security_protocol", "SASL_SSL")
        .add_settings("sasl_mechanism", "SCRAM-SHA-256")
        .add_settings("username", "readonly")
        .add_settings("password", external_stream_password)
        .add_settings("skip_ssl_cert_check", "1")

        .add_settings("topic", "car_live_data")
        .create()
    )

    stream_list = ExternalStream(env=test_environment).list()
    assert name in [q.name for q in stream_list]

    get_stream = ExternalStream(env=test_environment).name(name).get()
    assert get_stream.metadata().name == name

    # Check the stream exists
    assert ExternalStream(env=test_environment).name(name).exist()

    stream.delete()
    stream_list = ExternalStream(env=test_environment).list()
    assert name not in [q.name for q in stream_list]

    # Ensure stream doesn't exist anymore
    assert not ExternalStream(env=test_environment).name(name).exist()
