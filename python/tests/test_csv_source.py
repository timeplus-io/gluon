import time
from rx import operators as ops

from timeplus import (
    CSVSource,
    SourceConnection,
    Query,
    Source,
    Stream,
)


def test_csv_source(test_environment):
    stream_name = "csv"

    try:
        Stream().name(stream_name).delete()
    except Exception:
        pass

    time.sleep(1)

    source = (
        CSVSource()
        .name("csv")
        .path(
            "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
        )
    )

    sourceConnection = (
        SourceConnection()
        .stream_definition(Stream().name(stream_name))
        .auto_create(True)
    )
    source.connection(sourceConnection)

    previewResult = source.preview()
    assert previewResult is not None

    source.create()

    sourceIds = [s.id() for s in Source.list()]
    assert source.id() in sourceIds
    assert source.stat()["status"] in ["running", "finished"]

    # still need to wait the stream to be created by source
    # read csv make take more time here
    time.sleep(5)

    streams = [ss.name() for ss in Stream.list()]
    assert stream_name in streams

    query = Query().sql(f"select * from table({stream_name})")
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
