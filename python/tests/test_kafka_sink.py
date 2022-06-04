import os
from datetime import datetime
import pytest

from kafka import KafkaConsumer

from timeplus import (
    KafkaProperties,
    KafkaSink,
    Query,
    Sink,
)


@pytest.mark.skip(reason="skip")
def test_confluent_kafka_sink(test_environment, confluent_broker):
    sink_topic = "timeplus_test_sink"

    query = Query().sql("select * from car_live_data")
    query.create()

    sink = (
        KafkaSink()
        .name("kafka")
        .properties(
            KafkaProperties()
            .topic(sink_topic)
            .brokers(confluent_broker)
            .sasl("plain")
            .username(os.environ.get("KAFKA_USER"))
            .password(os.environ.get("KAFKA_PASS"))
        )
    )
    sink.create()
    query.sink_to(sink)

    consumer = KafkaConsumer(
        sink_topic,
        bootstrap_servers=confluent_broker,
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

    sink.delete()
    sinkIds = [s.id() for s in Sink.list()]
    assert sink.id() not in sinkIds

    query.delete()


def test_no_auth_kafka_sink(test_environment, demo_broker):
    sink_topic = "timeplus_test_sink"

    query = Query().sql("select * from car_live_data")
    query.create()

    sink = (
        KafkaSink()
        .name("kafka")
        .properties(
            KafkaProperties()
            .topic(sink_topic)
            .brokers(demo_broker)
            .sasl("none")
            .replication_factor(1)
            .partition_number(1)
        )
    )
    sink.create()
    query.sink_to(sink)

    consumer = KafkaConsumer(
        sink_topic,
        bootstrap_servers=demo_broker,
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

    sink.delete()
    sinkIds = [s.id() for s in Sink.list()]
    assert sink.id() not in sinkIds

    query.delete()
