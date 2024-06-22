def test_dbapi_table(conn, test_stream):
    cursor = conn.execute("select * from table(test_stream)")
    next_result = cursor.next()
    row1 = cursor.fetchone()
    assert next_result is not None
    assert row1 is not None

    rows = cursor.fetchmany(2)
    assert len(rows) == 2

    cursor_2 = conn.execute("select 1<>2")
    query_result = list(cursor_2)
    assert len(query_result) == 1


def test_dbapi_live(conn, test_stream):
    cursor = conn.execute("select * from test_stream where _tp_time > earliest_ts()")
    next_result = cursor.next()
    row1 = cursor.fetchone()
    rows = cursor.fetchmany(2)

    assert next_result is not None
    assert row1 is not None
    assert len(rows) == 2


def test_dbapi_show_streams(conn, test_stream):
    cursor = conn.execute("show streams")
    row = cursor.fetchone()

    assert row is not None
