import json
import time

from timeplus import Query


def test_query_with_stream(test_environment, test_stream):
    # Test the Query object with stream
    query = (
        Query(env=test_environment)
        .sql(query=f"SELECT * FROM test_stream")
        .create()
    )

    query_id = query.id()

    query_list = Query(env=test_environment).list()
    assert query_id in [q.id for q in query_list]

    metadata = query.metadata()
    assert "name" in metadata
    assert "sql" in metadata
    assert "id" in metadata

    query.cancel()
    # Without query.cancel(), there will be an error:
    # OSError: [Errno 9] Bad file descriptor And the query cannot be deleted
    query.delete()

    query_list = Query(env=test_environment).list()
    assert query_id not in [q.id for q in query_list]


def test_query_with_table(test_environment, test_stream):
    #Test the Query Object with history table
    data = [["time", "data"], [[1, "efgh"]]]
    test_stream.ingest(*data)

    time.sleep(3)
    # Without sleep(3), there will be an error:
    # FAILED test_query.py::test_query_with_table - KeyError: 'id'

    query = (
        Query(env=test_environment)
        .sql(query="SELECT * FROM table(test_stream)")
        .create()
    )

    limit = 2
    count = 0

    results = []
    for event in query.result():
        if event.event == "message":
            results.extend(json.loads(event.data))
        count += 1
        if count >= limit:
            break
    print(results)
    assert len(results) == 2
    query.delete()
