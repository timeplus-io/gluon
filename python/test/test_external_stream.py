from timeplus import ExternalStream


def test_external_stream(test_environment):
    name = "gluon_test_external_name"

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
        .add_settings("brokers", "kafka.demo-internal:9092")
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
