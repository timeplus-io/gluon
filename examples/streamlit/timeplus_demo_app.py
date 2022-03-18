import streamlit as st

import time
import os

import pandas as pd
import numpy as np

from timeplus import (
    Stream,
    Query,
    Env,
    Source,
    Stopper,
    StreamColumn,
    KafkaSource,
    KafkaSink,
    KafkaProperties,
    SourceConnection,
    GeneratorConfiguration,
    GeneratorField,
    GeneratorSource,
    SourceConnection,
    SlackSink,
    SlackSinkProperty,
    SMTPSink,
    SMTPSinkProperty,
)
from rx import operators as ops

st.title("Timeplus Platform")
st.write("Fast + powerful real-time analytics made intuitive.")
st.write("See https://timeplus.com")

## Environment
client_id = os.environ.get("AUTH0_API_CLIENT_ID")
client_secret = os.environ.get("AUTH0_API_CLIENT_SECRET")
env = (
    Env()
    .schema("https")
    .host("staging.demo.timeplus.io")
    .port("443")
    .login(client_id=client_id, client_secret=client_secret)
)
Env.setCurrent(env)
st.write(env.info())

## Query

# query_sql = "select * from car_live_data"
# st.write(f"run query of {query_sql}")

# s = Stream().name("car_live_data").get()
# query = Query().sql(query_sql).create()

# time.sleep(5)
# st.write(query.stat())
# st.write(f"query {query.id()} is {query.status()}")
# st.write([h["name"] for h in query.header()])

# stopper = Stopper()
# query.get_result_stream(stopper).pipe(ops.take(3)).subscribe(
#     on_next=lambda i: st.write(f"get one result {i}"),
#     on_error=lambda e: print(f"error {e}"),
#     on_completed=lambda: stopper.stop(),
# )

# query.cancel()
# st.write(f"query {query.id()} is {query.status()}")
# query.delete()

## Stream
# st.write(f"demo stream inferface")
# s = (
#     Stream()
#     .name("demo_stream")
#     .column(StreamColumn().name("a").type("String"))
#     .column(StreamColumn().name("b").type("Float64"))
# )

# s.create()
# st.write(f"stream {s.name()} is created")

# streams = [ss.name() for ss in Stream.list()]
# st.write(f"current streams are {streams}")

# st.write(f"inserting data to stream {s.name()}")
# s.insert([["a", 100.1], ["b", 200.2]])

# time.sleep(5)

# query = Query().name("ad hoc query").sql(f"select * from table({s.name()})").create()
# stopper = Stopper()
# result = []
# query.get_result_stream(stopper).pipe(ops.take(2)).subscribe(
#     on_next=lambda i: st.write(f"get one result {i}"),
#     on_error=lambda e: print(f"error {e}"),
#     on_completed=lambda: stopper.stop(),
# )

#st.write(f"deleting stream {s.name()}")
#s.delete()
# streams = [ss.name() for ss in Stream.list()]
# st.write(f"current streams are {streams}")

## Source/Sink

#### kafka
# topic = "datagen"
# brokers = "pkc-ld537.ca-central-1.aws.confluent.cloud:9092"
# sasl = "plain"
# username = "E2YTK4EBCA6UP7NX"
# password = "0oIxM8juTDxGZ14IFpXbIM6kTsSejOSFtlVm9sOzRVvknTFh8Ohwl5xHW3WuL4ai"

# source = (
#     KafkaSource()
#     .name("kafka")
#     .properties(
#         KafkaProperties()
#         .topic(topic)
#         .brokers(brokers)
#         .sasl(sasl)
#         .username(username)
#         .password(password)
#     )
# )
# source.connection(SourceConnection().stream("confluent_datagen").auto_create(True))

# st.write("kafka source preview")
# st.write(source.preview())

# source.create().start()
# st.write("kafka source created")

# s = Stream().name("confluent_datagen").get()
# st.write(s.data())

# time.sleep(2)
# st.write(f"kafka source status {source.get().stat()}")
# time.sleep(2)
# st.write(f"kafka source status {source.get().stat()}")
# time.sleep(2)
# st.write(f"kafka source status {source.get().stat()}")

# query = Query().name("ad hoc query").sql(f"select * from confluent_datagen").create()

# topic = "datagen_sink"
# brokers = "pkc-ld537.ca-central-1.aws.confluent.cloud:9092"
# sasl = "plain"
# username = "E2YTK4EBCA6UP7NX"
# password = "0oIxM8juTDxGZ14IFpXbIM6kTsSejOSFtlVm9sOzRVvknTFh8Ohwl5xHW3WuL4ai"

# sink = (
#     KafkaSink()
#     .name("kafka sink")
#     .properties(
#         KafkaProperties()
#         .topic(topic)
#         .brokers(brokers)
#         .sasl(sasl)
#         .username(username)
#         .password(password)
#     )
# )

# sink.create()
# query.sink_to(sink)

# stopper = Stopper()
# query.get_result_stream(stopper).pipe(ops.take(5)).subscribe(
#     on_next=lambda i: st.write(f"get one result {i}"),
#     on_error=lambda e: print(f"error {e}"),
#     on_completed=lambda: stopper.stop(),
# )


# sink.delete()
# source.delete()
# query.delete()

## clean all source here
# for s in Source.list():
#     st.write(s.id())
#     s.delete()

#### Generator to Slack

# config = (
#     GeneratorConfiguration()
#     .batch(1)
#     .interval(200)
#     .field(GeneratorField().name("number").type("int").limit([0, 10]))
#     .field(
#         GeneratorField()
#         .name("time")
#         .type("timestamp")
#         .timestamp_format("2006-01-02 15:04:05.000")
#     )
# )

# sourceConnection = (
#     SourceConnection().stream("clicks").auto_create(True).event_time_column("time")
# )
# source = (
#     GeneratorSource()
#     .name("click stream")
#     .type("stream_generator")
#     .connection(sourceConnection)
#     .config(config)
# )

# st.write("generator source preview")
# st.write(source.preview())

# source.create().start()
# st.write("generator source created")

# sink = (
#     SlackSink()
#     .name("slack sink")
#     .properties(
#         SlackSinkProperty()
#         .url(
#             "https://hooks.slack.com/services/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"
#         )
#         .message(
#             "You have a new alert click count {{.number}}:\n*<fakeLink.timeplus.com|Gang Tao - New Alert>*"
#         )
#     )
# )
# sink.create()

# sink = (
#     SMTPSink()
#     .name("email sink")
#     .properties(
#         SMTPSinkProperty()
#         .f("eng@timeplus.io")
#         .to("gang.tao@outlook.com")
#         .username("AKIA264B774K6MEAKUOY")
#         .password("BJTl500n0eOd+e94BNuHiut2DuDXo3y34PnGChre19Zq")
#         .host("email-smtp.us-west-1.amazonaws.com")
#         .port(587)
#         .message("You have a new alert at {{.time}} with click count {{.number}}")
#     )
# )

# sink.create()
# st.write(f"{sink.get().data()}")

# query = (
#     Query().name("ad hoc query").sql(f"select * from clicks where number > 4").create()
# )
# query.sink_to(sink)

# stopper = Stopper()
# query.get_result_stream(stopper).pipe(ops.take(5)).subscribe(
#     on_next=lambda i: st.write(f"get one result {i}"),
#     on_error=lambda e: print(f"error {e}"),
#     on_completed=lambda: stopper.stop(),
# )

# source.delete()
# query.delete()
# st.write("generator source deleted")

# for q in Query.list():
#     q.cancel().delete()
