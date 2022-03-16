import time
from rx import operators as ops

from timeplus import Stream, StreamColumn, Query, Stopper, Env


def test_stream():
    env = Env()
    env.schema("https").host("kafka1.dev.timeplus.io").port("443").login()

    s = (
        Stream(env=env)
        .name("abc")
        .column(StreamColumn().name("a").type("String"))
        .column(StreamColumn().name("b").type("Float64"))
    )

    s.delete()
    time.sleep(1)

    streams = [ss.name() for ss in Stream.list(env=env)]
    assert s.name() not in streams

    s.create()
    streams = [ss.name() for ss in Stream.list(env=env)]
    assert s.name() in streams

    s.insert([["a", 100.1], ["b", 200.2]])

    time.sleep(3)
    query = Query(env=env).name("ad hoc query").sql("select * from table(abc)").create()

    stopper = Stopper()
    result = []
    query.get_result_stream(stopper).pipe(ops.take(2)).subscribe(
        on_next=lambda i: result.append(i),
        on_error=lambda e: print(f"error {e}"),
        on_completed=lambda: stopper.stop(),
    )

    assert len(result) == 2

    s.delete()

    time.sleep(1)  # delete stream still need to wait

    streams = [ss.name() for ss in Stream.list(env=env)]
    assert s.name() not in streams