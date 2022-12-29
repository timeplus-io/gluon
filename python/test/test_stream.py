from timeplus import Stream


def test_stream(test_environment):
    stream_list = Stream(env=test_environment).list()
    count = len(stream_list)

    name = "test_test_test"

    # create a new stream
    stream = (
        Stream(env=test_environment)
        .name(name)
        .column("time", "datetime64(3)")
        .column("data", "string")
        .create()
    )

    stream_list = Stream(env=test_environment).list()
    count1 = len(stream_list)

    assert count1 == count + 1

    stream.delete()
    stream_list = Stream(env=test_environment).list()
    count2 = len(stream_list)
    assert count2 == count
