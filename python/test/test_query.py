from timeplus import Stream, Query
from timeplus.error import TimeplusAPIError


def test_query_with_stream(test_environment, test_stream):
    # Test the Query object
    query_list = Query(env=test_environment).list()
    count = len(query_list)

    query = (
        Query(env=test_environment)
        .sql(query=f"SELECT * FROM test_stream")
        .create()
    )

    query_list = Query(env=test_environment).list()
    count1 = len(query_list)

    assert count1 == count + 1
    metadata = query.metadata()
    assert "name" in metadata
    assert "sql" in metadata
    assert "id" in metadata

    query_id = query.id
    query.delete()
    test_stream.delete()

    query_list = Query(env=test_environment).list()
    assert query_id not in [q.id for q in query_list]

