from timeplus import Query


def test_analyze(test_environment):
    result = (
        Query(env=test_environment)
        .sql(query=f"SELECT * FROM car_live_data")
        .analyze()
    )

    assert result is not None
