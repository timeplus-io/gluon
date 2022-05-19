import time
from datetime import datetime
from rx import operators as ops

from timeplus import Stream, StreamColumn, Query, Type
from timeplus.utils import toDate


def test_stream(test_environment):
    s = (
        Stream()
        .name("datagen")
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

    try:
        s.delete()
    except Exception as e:
        pass

    time.sleep(3)

    streams = [ss.name() for ss in Stream.list()]
    assert s.name() not in streams

    s.create()
    streams = [ss.name() for ss in Stream.list()]
    assert s.name() in streams

    s.insert(
        [
            [
                10,
                10.23,
                12.5678,
                True,
                "hello world",
                toDate(datetime.now()),
                datetime.now(),
                datetime.now(),
                ["a", "b"],
                {"a": 1, "b": 2},
                ("a", 1, False),
            ],
            [
                11,
                12.23,
                13.5678,
                False,
                "hello timepluse",
                "2022-03-23",
                datetime.now(),
                datetime.now(),
                ["c", "d"],
                {"a": 2, "b": 3},
                ("abc", 3, True),
            ],
        ]
    )

    time.sleep(3)
    query = (
        Query().name("ad hoc query").sql(f"select * from table({s.name()})").create()
    )

    result = []
    query.get_result_stream().pipe(ops.take(2)).subscribe(
        on_next=lambda i: result.append(i),
        on_error=lambda e: print(f"error {e}"),
        on_completed=lambda: query.stop(),
    )

    assert len(result) == 2

    test_environment.logger().info("result header is {}", query.header())
    test_environment.logger().info("result data is {}", result)

    for r in result:
        test_environment._logger.info("record data is {}", r)

    s.delete()

    time.sleep(1)  # delete stream still need to wait

    streams = [ss.name() for ss in Stream.list()]
    assert s.name() not in streams
