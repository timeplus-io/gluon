import json

from timeplus import Stream, Query
from timeplus.error import TimeplusAPIError


def test_query_with_stream(test_environment, test_stream):
    # Test the Query object
    query_list_before = Query(env=test_environment).list()
    count = len(query_list_before)

    query = (
        Query(env=test_environment)
        .sql(query=f"SELECT * FROM test_stream")
        .create()
    )

    metadata = query.metadata()
    assert "name" in metadata
    assert "sql" in metadata

    query_list_after = Query(env=test_environment).list()
    count1 = len(query_list_after)

    assert count1 == count + 1

    query.delete()
    test_stream.delete()

    query_list_final = Query(env=test_environment).list()
    count2 = len(query_list_final)

    assert count2 == count


