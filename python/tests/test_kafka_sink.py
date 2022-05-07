import time
import os
from datetime import datetime

from kafka import KafkaConsumer

from timeplus import (
    KafkaProperties,
    KafkaSink,
    KafkaSource,
    SourceConnection,
    Query,
    Source,
    Sink,
    Stream,
)


def test_kafka_sink(staging_environment, test_broker):
    stream_name = "covid19"
    source_topic = "covid19"
    sink_topic = "covid19_sink"

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
            .brokers(test_broker)
            .sasl("plain")
            .username(os.environ.get("KAFKA_USER"))
            .password(os.environ.get("KAFKA_PASS"))
            .offset("earliest")
            .group("testgroup" + str(time.time()))
        )
    )

    sourceConnection = SourceConnection().stream(stream_name).auto_create(True)
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

    query = Query().sql(f"select * from {stream_name} SETTINGS seek_to='earliest'")
    query.create()

    sink = (
        KafkaSink()
        .name("kafka")
        .properties(
            KafkaProperties()
            .topic(sink_topic)
            .brokers(test_broker)
            .sasl("plain")
            .username(os.environ.get("KAFKA_USER"))
            .password(os.environ.get("KAFKA_PASS"))
        )
    )
    sink.create()
    query.sink_to(sink)

    consumer = KafkaConsumer(
        sink_topic,
        bootstrap_servers=test_broker,
        security_protocol="SASL_SSL",
        sasl_mechanism="PLAIN",
        sasl_plain_username=os.environ.get("KAFKA_USER"),
        sasl_plain_password=os.environ.get("KAFKA_PASS"),
        auto_offset_reset="latest",
        enable_auto_commit=False,
    )

    start_time = datetime.now()
    count = 0
    for msg in consumer:
        count += 1
        if count % 100 == 0:
            end_time = datetime.now()
            print(count / (end_time - start_time).total_seconds())
        if count > 1000:
            break
    assert count > 1000

    source.delete()
    sourceIds = [s.id() for s in Source.list()]
    assert source.id() not in sourceIds

    sink.delete()
    sinkIds = [s.id() for s in Sink.list()]
    assert sink.id() not in sinkIds

    query.delete()
