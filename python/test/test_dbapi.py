import os
from timeplus.dbapi import connect


def test_dbapi_table():
    api_key = os.environ.get("TIMEPLUS_API_KEY")
    api_address = "dev.timeplus.cloud"
    workspace = os.environ.get("TIMEPLUS_WORKSPACE")
    conn = connect(host=api_address, password=api_key, path=workspace)

    cusor = conn.execute("select * from table(car_live_data)")
    next_result = cusor.next()
    row1 = cusor.fetchone()
    rows = cusor.fetchmany(3)
    cusor_2 = conn.execute("select 1<>2")
    query_result = list(cusor_2)

    assert next_result is not None
    assert row1 is not None
    assert len(rows) == 3
    assert len(query_result) == 1


def test_dbapi_live():
    api_key = os.environ.get("TIMEPLUS_API_KEY")
    api_address = "dev.timeplus.cloud"
    workspace = os.environ.get("TIMEPLUS_WORKSPACE")
    conn = connect(host=api_address, password=api_key, path=workspace)

    cusor = conn.execute("select * from car_live_data")
    next_result = cusor.next()
    row1 = cusor.fetchone()
    rows = cusor.fetchmany(3)
    cusor_2 = conn.execute("select 1<>2")
    query_result = list(cusor_2)

    assert next_result is not None
    assert row1 is not None
    assert len(rows) == 3
    assert len(query_result) == 1