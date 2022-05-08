import time
from rx import operators as ops
import pytest

from timeplus import (
    GeneratorConfiguration,
    GeneratorField,
    GeneratorSource,
    SourceConnection,
    Query,
    Source,
    Stream,
)


def test_generator_source(staging_environment):
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
    sourceConnection = (
        SourceConnection()
        .stream(stream_name)
        .auto_create(True)
        .event_time_column("time")
    )

    source = (
        GeneratorSource()
        .name("click stream")
        .connection(sourceConnection)
        .config(config)
    )

    source.create().start()
    sourceIds = [s.id() for s in Source.list()]
    assert source.id() in sourceIds

    # still need to wait the stream to be created by source
    time.sleep(3)

    streams = [ss.name() for ss in Stream.list()]
    assert stream_name in streams

    query = Query().sql(f"select * from {stream_name}")
    query.create()

    result = []
    query.get_result_stream().pipe(ops.take(5)).subscribe(
        on_next=lambda i: result.append(i),
        on_error=lambda e: print(f"error {e}"),
        on_completed=lambda: query.stop(),
    )

    assert len(result) == 5
    source.delete()
    sourceIds = [s.id() for s in Source.list()]
    assert source.id() not in sourceIds

    query.delete()


@pytest.mark.skip(reason="skip")
def test_dataset_source(local_environment):
    stream_name = "dataset"

    try:
        Stream().name(stream_name).delete()
    except Exception:
        pass

    time.sleep(1)

    config = GeneratorConfiguration().batch(1).interval(200).datasets("creditcardfraud")
    sourceConnection = SourceConnection().stream(stream_name).auto_create(True)

    source = (
        GeneratorSource()
        .name("click stream")
        .connection(sourceConnection)
        .config(config)
    )

    source.create().start()
    sourceIds = [s.id() for s in Source.list()]
    assert source.id() in sourceIds

    # still need to wait the stream to be created by source
    time.sleep(3)

    streams = [ss.name() for ss in Stream.list()]
    assert stream_name in streams

    query = Query().sql(f"select * from {stream_name}")
    query.create()

    result = []
    query.get_result_stream().pipe(ops.take(5)).subscribe(
        on_next=lambda i: result.append(i),
        on_error=lambda e: print(f"error {e}"),
        on_completed=lambda: query.stop(),
    )

    assert len(result) == 5
    source.delete()
    sourceIds = [s.id() for s in Source.list()]
    assert source.id() not in sourceIds

    query.delete()
