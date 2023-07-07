from timeplus import Stream, Query
from timeplus.error import TimeplusAPIError


def test_query_with_stream(test_environment, test_table):
    # Test the Query object
    query_list = Query(env=test_environment).list()
    count = len(query_list)

    query = (
        Query(env=test_environment)
        .sql(query=f"SELECT * FROM {test_table}")
        .create()
    )

    query_list = Query(env=test_environment).list()
    count1 = len(query_list)

    assert count1 == count + 1

    query_result = query.run()

    assert len(query_result) == 10

    query.delete()
    query_list = Query(env=test_environment).list()
    count2 = len(query_list)

    assert count2 == count


def test_invalid_query_with_stream(test_environment, test_table):
    # Test an invalid query
    query = (
        Query(env=test_environment)
        .sql(query="SELECT * FROM non_existent_table")
        .create()
    )

    try:
        query.run()
        assert False, "Expected an exception when running an invalid query"
    except TimeplusAPIError:
        pass  # Expected

    query.delete()


def test_stream_columns(test_environment, test_table):
    # Test the columns of the stream
    assert test_table.columns() == [("id", "integer"), ("data", "string")]


def test_stream_exists(test_environment, test_table):
    # Test if the stream exists
    assert Stream(env=test_environment).name(test_table.name).exists() == True


def test_query_execution(test_environment, test_table):
    # Test the execution of a query
    query = (
        Query(env=test_environment)
        .sql(query=f"SELECT * FROM {test_table.name}")
        .create()
    )

    result = query.run()

    assert len(result) == 10


def test_query_data_return(test_environment, test_table):
    query = (
        Query(env=test_environment)
        .sql(query=f"SELECT data FROM {test_table.name} WHERE id = 0")
        .create()
    )

    result = query.run()

    assert "random_string_" in result[0]['data']


def test_query_nonexistent_stream(test_environment):
    # Test a query on a nonexistent stream
    query = (
        Query(env=test_environment)
        .sql(query="SELECT * FROM nonexistent_stream")
        .create()
    )

    try:
        query.run()
        assert False, "Expected an error when trying to run a query on a nonexistent stream"
    except TimeplusAPIError:
        pass  # Expected
