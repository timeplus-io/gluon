from timeplus import Query


def test_analyze(test_environment, test_stream):
    result = (
        Query(env=test_environment)
        .sql(query=f"SELECT * FROM test_stream")
        .analyze()
    )

    assert result is not None
