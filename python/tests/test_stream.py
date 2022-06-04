import time
from datetime import datetime
from rx import operators as ops

from timeplus import Stream, StreamColumn, Query


def test_stream(test_environment):
    s = (
        Stream()
        .name("abc")
        .column(StreamColumn().name("a").type("string"))
        .column(StreamColumn().name("b").type("float64"))
        .column(StreamColumn().name("t0").type("datetime64"))
        .column(StreamColumn().name("t1").type("datetime64(3)"))
        .column(StreamColumn().name("t2").type("datetime64(6)"))
        .column(StreamColumn().name("_time").type("datetime64(3)"))
    )

    try:
        s.delete()
    except Exception as e:
        pass

    time.sleep(1)

    streams = [ss.name() for ss in Stream.list()]
    assert s.name() not in streams

    s.create()
    streams = [ss.name() for ss in Stream.list()]
    assert s.name() in streams

    s.insert(
        [
            [
                "aaa string",
                100.1,
                "2022-03-31 23:16:47.743",
                datetime.now(),
                datetime.now(),
                "2022-03-31 23:16:47.743",
            ],
            [
                "bbb string",
                200.2,
                int(time.time() * 1000),
                int(time.time() * 1000),
                int(time.time() * 1000 * 1000),
                "2022-03-31 23:16:47.743",
            ],
        ]
    )

    time.sleep(3)
    query = Query().name("ad hoc query").sql("select * from table(abc)").create()

    result = []
    query.get_result_stream().pipe(ops.take(2)).subscribe(
        on_next=lambda i: result.append(i),
        on_error=lambda e: print(f"error {e}"),
        on_completed=lambda: query.stop(),
    )

    assert len(result) == 2

    s.delete()

    time.sleep(1)  # delete stream still need to wait

    streams = [ss.name() for ss in Stream.list()]
    assert s.name() not in streams
