import pytest
from rx import operators as ops
from timeplus import Query


def test_query(test_environment):
    query = (
        Query()
        .name("ad hoc query")
        .sql(
            "select time, gas_percent, speed_kmh from car_live_data where cid='c00004'"
        )
    )
    query.create()

    result = []
    query.get_result_stream().pipe(ops.take(3)).subscribe(
        on_next=lambda i: result.append(i),
        on_error=lambda e: print(f"error {e}"),
        on_completed=lambda: query.stop(),
    )

    assert len(result) == 3
    query.delete()


def test_query_to_sync(test_environment):
    sql = "select * from table(car_live_data) where cid='c00004' limit 2"
    result = Query.execSQL(sql)

    assert len(result["data"]) == 2
    assert result["header"] is not None


def test_invalid_query_to_sync(test_environment):
    sql = "select xyz "
    with pytest.raises(Exception) as e:
        Query.execSQL(sql)


def test_query_timeout(test_environment):
    sql = "select * from car_live_data"
    result = Query.execSQL(sql, timeout=1)

    assert result["header"] is not None
    assert len(result["data"]) > 0
