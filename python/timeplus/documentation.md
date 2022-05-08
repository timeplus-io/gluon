

## What is Timeplus

Timeplus is a purpose-built streaming analytics platform that solves enterprises’ need for easy-to-implement real-time analytics. Timeplus adapts a streaming-first architecture to redesign real-time analytics from ingestion to action, helping enterprises analyze massive sets of streaming data faster. We provide a dynamic schema for real-time analytics, bringing unprecedented flexibility to data querying and processing. This empowers enterprises to extract substantial value from data before it goes obsolete. Timeplus is unique in its features and functionality, enabling users to make real-time analytics:

- **Fast**: Users can run lightning-fast analytics with ultra-low latency, while ensuring extremely high EPS (events-per-second), both with ingestion and query simultaneously. Our testing demonstrates highly compelling results: Timeplus can achieve 4 millisecond end-to-end latency, and 10 million + EPS benchmark even in a single commodity machine.

- **Powerful**: Users can quickly analyze real-time streaming data, while simultaneously connecting to historical data assets. We use a converged multi-tier computation engine, which reduces data redundancy while substantially lowering costs. We’ve developed powerful real-time streaming analytics that enable functionality such as windowing/non-windowing, late event, downsampling and streaming predictive analytics. All from one SQL query.

- **Intuitive**: Users get speed, ease-of-use, and advanced analytics functions, both in the cloud or at the edge, and can quickly act on data simultaneously as it arrives. Once various data sources are connected, users can immediately explore streaming patterns via query and visualization, and create real-time multi-channel notifications, or send insights or aggregated data to the downstream systems. Powered by ultra-low latency of streaming processing, HFR (High-Frame-Rate) charts and dashboards can automatically update at real-time, so users can say goodbye to refresh and reload, and other slow and cumbersome user experiences.

For more information, refer to :
- [Timeplus Website](https://www.timeplus.com/)
- [Timeplus Linkedin](https://www.linkedin.com/company/timeplusinc/)
- [Timeplus Playground](https://play.timeplus.com/playground)
- [Timeplus Documentation](https://docs.timeplus.com/)
- [Timeplus Slack](https://timepluscommunity.slack.com/)
- [Timeplus Medium](https://medium.com/www-timeplus-com)
- [Join Timeplus Beta](https://www.timeplus.com/) 


## Installation

run `pip install timeplus` 

## Quick Start

The following sample code show how to create a timeplus environment, create a stream, insert event into stream, delete the stream and query an existing stream from timeplus.

```python
from rx import operators as ops
from timeplus import Stream, StreamColumn, Query, Env

# initialize timeplus environment
token = os.environ.get("TIMEPLUS_API_TOKEN")
env = (
    Env().schema("https").host("hostname").port("443").token(token)
)
Env.setCurrent(env)

# create a stream
s = (
    Stream()
    .name("stream_name")
    .column(StreamColumn().name("field_name_a").type("string"))
    .column(StreamColumn().name("field_name_b").type("float64"))
)

s.create()

# insert data into stream
s.insert(
    [
        [
            "hello",
            100.1
        ],
        [
            "timeplus",
            20.2
        ],
    ]
)

# delete stream
s.delete()

# run query on existing stream
query = Query().sql(f"select * from stream_name")
query.create()

query.get_result_stream().pipe(ops.take(5)).subscribe(
    on_next=lambda i: print(f"get one query result {i}"),
    on_error=lambda e: print(f"error {e}"),
    on_completed=lambda: query.stop(),
)
```

## Environment

The `Env` is class encapsulate the information how to access a timeplus deployment, user can have multiple `Env` instance and switch between them.  

The `Env` has following properties:
- `schema` http or https
- `host` timeplus host 
- `port` timeplus port
- `token` access token, the user can find the token from the help page of timeplus console

due to the current token will expire, in case to support auto refresh token, set `audience`, `client_id` and `client_secret` to enable auto token refresh. The maximum refresh is set to `24`

```
env = Env()
env.audience(os.environ.get("TIMEPLUS_AUDIENCE"))
env.client_id(os.environ.get("TIMEPLUS_API_CLIENT_ID"))
env.client_secret(os.environ.get("TIMEPLUS_API_CLIENT_SECRET"))
```

## Stream

Similar as traditional database table, a [stream](https://docs.timeplus.com/docs/working-with-streams) is where the stream data stored in Timeplus. 

## Query

Timeplus provide [stream query](https://docs.timeplus.com/docs/stream-query) which is following the SQL semantic, a unbounded query that can be easily used to analysis streaming data.

The stream query result is sending to user through websocket, the SDK has encapsulated it with a result stream using [reactivX for python](https://github.com/ReactiveX/RxPY). the user can use all reactiveX operators to manipulate the result stream.

## Source

Timeplus support loading stream data from differet [sources](https://docs.timeplus.com/docs/source) including:
- Apache Kafka ( Redpanda )
- CSV File
- Stream Generator

## Sink

Timeplus support export stream query result to down stream destinations called [sink](https://docs.timeplus.com/docs/destination), including:
- Apache Kafka
- Email
- Slack
