from timeplus import Source, Stream


def test_source(test_environment):
    stream_name = "iot"

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
    source_name = "iot"
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
    source_id = source.metadata().id
    assert source_name in [q.name for q in source_list]

    assert Source(env=test_environment).name(source_name).exist(source_id)

    assert Source(env=test_environment).name(source_name).exist(source_id)
    source.delete(source_id)
    stream.delete()

    source_list = Source(env=test_environment).list()
    assert source_name not in [s.name for s in source_list]

    assert not Source(env=test_environment).name(source_name).exist(source_id)