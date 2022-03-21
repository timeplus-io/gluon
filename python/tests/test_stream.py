import time
from datetime import datetime
from rx import operators as ops

from timeplus import Stream, StreamColumn, Query, Stopper


def test_stream(staging_environment):
    s = (
        Stream()
        .name("abc")
        .column(StreamColumn().name("a").type("String"))
        .column(StreamColumn().name("b").type("Float64"))
        .column(StreamColumn().name("t0").type("Datetime64"))
        .column(StreamColumn().name("t1").type("Datetime64(3)"))
        .column(StreamColumn().name("t2").type("Datetime64(6)"))
    )

    s.delete()
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
                datetime.now(),
                datetime.now(),
                datetime.now(),
            ],
            [
                "bbb string",
                200.2,
                int(time.time() * 1000),
                int(time.time() * 1000),
                int(time.time() * 1000 * 1000),
            ],
        ]
    )

    time.sleep(3)
    query = Query().name("ad hoc query").sql("select * from table(abc)").create()

    stopper = Stopper()
    result = []
    query.get_result_stream(stopper).pipe(ops.take(2)).subscribe(
        on_next=lambda i: result.append(i),
        on_error=lambda e: print(f"error {e}"),
        on_completed=lambda: stopper.stop(),
    )

    assert len(result) == 2

    # s.delete()

    # time.sleep(1)  # delete stream still need to wait

    # streams = [ss.name() for ss in Stream.list()]
    # assert s.name() not in streams
