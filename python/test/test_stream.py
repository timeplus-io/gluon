from timeplus import Stream


def test_stream(test_environment):
    name = "test_test_test"

    # Create a new stream instance with the given name
    stream = Stream(env=test_environment).name(name)

    try:
        stream.delete()
    except Exception:
        pass

    # create a new stream
    stream = (
        Stream(env=test_environment)
        .name(name)
        .column("time", "datetime64(3)")
        .column("data", "string")
        .create()
    )

    stream_list = Stream(env=test_environment).list()
    assert name in [q.name for q in stream_list]

    get_stream = Stream(env=test_environment).name(name).get()
    assert get_stream.metadata().name == name

    # Check the stream exists
    assert Stream(env=test_environment).name(name).exist()

    stream.delete()
    stream_list = Stream(env=test_environment).list()
    assert name not in [q.name for q in stream_list]

    # Ensure stream doesn't exist anymore
    assert not Stream(env=test_environment).name(name).exist()
