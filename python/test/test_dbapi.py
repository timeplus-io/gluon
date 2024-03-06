def test_dbapi_table(conn):
    cursor = conn.execute("select * from table(car_live_data)")
    next_result = cursor.next()
    row1 = cursor.fetchone()
    rows = cursor.fetchmany(3)
    cursor_2 = conn.execute("select 1<>2")
    query_result = list(cursor_2)

    assert next_result is not None
    assert row1 is not None
    assert len(rows) == 3
    assert len(query_result) == 1


def test_dbapi_live(conn):
    cursor = conn.execute("select * from car_live_data")
    next_result = cursor.next()
    row1 = cursor.fetchone()
    rows = cursor.fetchmany(3)
    cursor_2 = conn.execute("select 1<>2")
    query_result = list(cursor_2)

    assert next_result is not None
    assert row1 is not None
    assert len(rows) == 3
    assert len(query_result) == 1


def test_dbapi_show_streams(conn):
    cursor = conn.execute("show streams")
    cursor.next()
    row = cursor.fetchone()

    assert row is not None
