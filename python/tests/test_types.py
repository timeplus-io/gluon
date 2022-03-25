import time
from datetime import datetime
from rx import operators as ops

from timeplus import Stream, StreamColumn, Query, Stopper, Type


def test_stream(staging_environment):
    s = (
        Stream()
        .name("stream_with_all_types")
        .column(StreamColumn().name("c1").type(Type.Integer))
        .column(StreamColumn().name("c2").type(Type.Decimal, 4, 2))
        .column(StreamColumn().name("c3").type(Type.Float))
        .column(StreamColumn().name("c4").type(Type.Bool))
        .column(StreamColumn().name("c5").type(Type.String))
        .column(StreamColumn().name("c6").type(Type.Date))
        .column(StreamColumn().name("c7").type(Type.Datetime))
        .column(StreamColumn().name("c8").type(Type.Datetime64))
        .column(StreamColumn().name("c9").type(Type.Array, Type.String))
        .column(StreamColumn().name("c10").type(Type.Map, Type.String, Type.Integer))
        .column(
            StreamColumn()
            .name("c11")
            .type(Type.Tuple, Type.String, Type.Integer, Type.Bool)
        )
    )

    s.delete()
    time.sleep(1)

    streams = [ss.name() for ss in Stream.list()]
    assert s.name() not in streams

    s.create()
    streams = [ss.name() for ss in Stream.list()]
    assert s.name() in streams
