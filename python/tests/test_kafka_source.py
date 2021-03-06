import time
import os
from rx import operators as ops

import pytest

from timeplus import (
    KafkaProperties,
    KafkaSource,
    SourceConnection,
    Query,
    Source,
    Stream,
)


@pytest.mark.skip(reason="skip")
def test_kafka_source(test_environment, confluent_broker):
    stream_name = "github_events"
    source_topic = "github_events"

    try:
        Stream().name(stream_name).delete()
    except Exception:
        pass

    source = (
        KafkaSource()
        .name("kafka")
        .properties(
            KafkaProperties()
            .topic(source_topic)
            .brokers(confluent_broker)
            .sasl("plain")
            .username(os.environ.get("KAFKA_USER"))
            .password(os.environ.get("KAFKA_PASS"))
            .offset("earliest")
            .group("testgroup" + str(time.time()))
        )
    )

    stream = Stream().name(stream_name)
    sourceConnection = SourceConnection().auto_create(True).stream_definition(stream)
    source.connection(sourceConnection)

    source.create().start()
    sourceIds = [s.id() for s in Source.list()]
    assert source.id() in sourceIds

    # still need to wait the stream to be created by source
    time.sleep(5)

    sourceIds = [s.id() for s in Source.list()]
    assert source.id() in sourceIds

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
def test_no_auth_kafka_source(test_environment, demo_broker):
    stream_name = "test_orders"
    source_topic = "orders"

    try:
        Stream().name(stream_name).delete()
    except Exception:
        pass

    source = (
        KafkaSource()
        .name("kafka")
        .properties(
            KafkaProperties()
            .topic(source_topic)
            .brokers(demo_broker)
            .sasl("none")
            .offset("earliest")
            .group("testgroup" + str(time.time()))
            .disable_tls()
        )
    )

    stream = Stream().name(stream_name)

    sourceConnection = SourceConnection().auto_create(True).stream_definition(stream)
    source.connection(sourceConnection)

    source.create()
    sourceIds = [s.id() for s in Source.list()]
    assert source.id() in sourceIds
    assert source.stat()["status"] == "running"

    # still need to wait the stream to be created by source
    time.sleep(5)

    sourceIds = [s.id() for s in Source.list()]
    assert source.id() in sourceIds

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
