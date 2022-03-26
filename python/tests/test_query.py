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
)


def test_query(staging_environment):
    stream_name = "clicks"

    Stream().name(stream_name).delete()
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
        GeneratorSource()
        .name("click stream")
        .type("stream_generator")
        .connection(sourceConnection)
        .config(config)
    )

    source.create().start()
    sourceIds = [s.id() for s in Source.list()]
    assert source.id() in sourceIds

    # still need to wait the stream to be created by source
    time.sleep(3)

    query = Query().name("ad hoc query").sql(f"select * from {stream_name}")
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
    sourceIds = [s.id() for s in Source.list()]
    assert source.id() not in sourceIds

    query.delete()


def test_query1(staging_environment):
    query = (
        Query()
        .name("ad hoc query")
        .sql(
            "select time, gas_percent, speed_kmh from car_live_data where cid='c00004'"
        )
    )
    query.create()

    stopper = Stopper()
    result = []
    query.get_result_stream(stopper).pipe(ops.take(5)).subscribe(
        on_next=lambda i: result.append(i),
        on_error=lambda e: print(f"error {e}"),
        on_completed=lambda: stopper.stop(),
    )

    assert len(result) == 5
    query.delete()


def test_sync_query(staging_environment):
    result = Query.execSQL("select * from table(car_live_data) limit 2")
    assert result is not None
