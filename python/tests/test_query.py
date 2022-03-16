import time
from rx import operators as ops

from timeplus import (
    GeneratorConfiguration,
    GeneratorField,
    GeneratorSource,
    SourceConnection,
    Query,
    Source,
    Stopper,
    Stream,
    Env,
)


def test_query():
    env = Env()
    env.schema("https").host("kafka1.dev.timeplus.io").port("443").login()

    stream_name = "clicks"

    Stream(env=env).name(stream_name).delete()
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
    sourceConnection = (
        SourceConnection()
        .stream(stream_name)
        .auto_create(True)
        .event_time_column("time")
    )

    source = (
        GeneratorSource(env=env)
        .name("click stream")
        .type("stream_generator")
        .connection(sourceConnection)
        .config(config)
    )

    source.create().start()
    sourceIds = [s.id() for s in Source.list(env=env)]
    assert source.id() in sourceIds

    time.sleep(3)  ## still need to wait the stream to be created by source

    query = Query(env=env).name("ad hoc query").sql(f"select * from {stream_name}")
    query.create()

    stopper = Stopper()
    result = []
    query.get_result_stream(stopper).pipe(ops.take(5)).subscribe(
        on_next=lambda i: result.append(i),
        on_error=lambda e: print(f"error {e}"),
        on_completed=lambda: stopper.stop(),
    )

    assert len(result) == 5
    source.delete()
    sourceIds = [s.id() for s in Source.list(env=env)]
    assert source.id() not in sourceIds
