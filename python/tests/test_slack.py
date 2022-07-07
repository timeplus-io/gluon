import time

from timeplus import (
    GeneratorConfiguration,
    GeneratorField,
    GeneratorSource,
    SourceConnection,
    SlackSinkProperty,
    SlackSink,
    Query,
    Source,
    Stream,
)


def test_generator_source_to_email(test_environment):
    stream_name = "clicks"

    try:
        Stream().name(stream_name).delete()
    except Exception:
        pass

    time.sleep(1)

    config = (
        GeneratorConfiguration()
        .batch(1)
        .interval(200)
        .field(GeneratorField().name("number").type("int").limit([0, 10]))
        .field(
            GeneratorField()
            .name("time")
            .type("timestamp")
            .timestamp_format("2006-01-02 15:04:05.000")
        )
    )

    stream = Stream().name(stream_name).event_time_column("time")
    sourceConnection = SourceConnection().auto_create(True).stream_definition(stream)

    source = (
        GeneratorSource()
        .name("click stream")
        .connection(sourceConnection)
        .config(config)
    )

    source.create()
    sourceIds = [s.id() for s in Source.list()]
    assert source.id() in sourceIds

    # still need to wait the stream to be created by source
    time.sleep(3)

    streams = [ss.name() for ss in Stream.list()]
    assert stream_name in streams

    query = Query().sql(f"select * from {stream_name}")
    query.create()

    sink = (
        SlackSink()
        .name("slack")
        .properties(
            SlackSinkProperty()
            .url("http://slack.com/something")
            .message("a test message")
        )
    )
    sink.create()
    query.sink_to(sink)

    # TODO : validate slack message here

    source.delete()
    sourceIds = [s.id() for s in Source.list()]
    assert source.id() not in sourceIds

    query.delete()
