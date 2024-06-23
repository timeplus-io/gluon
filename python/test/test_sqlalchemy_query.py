import time
import pytest
from sqlalchemy import text, select, MetaData, Table
from datetime import timedelta
from timeplus import View


def test_driver_sql(engine, test_stream):
    with engine.connect() as conn:
        result = conn.exec_driver_sql(
            "select * from table(test_stream) limit 2")
        assert len(result.fetchall()) == 2


def test_driver_sql_live(engine, test_stream):
    with engine.connect() as conn:
        result = conn.exec_driver_sql(
            "select * from test_stream where _tp_time > earliest_ts() limit 2")
        assert len(result.fetchall()) == 2

def test_text_sql(engine, test_stream):
    with engine.connect() as connection:
        result = connection.execute(
            text("select * from table(test_stream) limit 3"))
        rows = [row for row in result]
        assert len(rows) == 3

def test_text_sql_live(engine, test_stream):
    with engine.connect() as connection:
        result = connection.execute(
            text("select * from test_stream where _tp_time > earliest_ts() limit 3"))
        rows = [row for row in result]
        assert len(rows) == 3

def test_text_streaming_sql(engine, test_stream):
    with engine.connect() as connection:
        result = connection.execute(text("select * from test_stream where _tp_time > earliest_ts()"))
        count = 0
        max = 3
        for row in result:
            assert row is not None
            count += 1
            if count >= max:
                break
        assert count == max

def test_check_stream_existence(engine, test_stream):
    table_name = "test_stream"
    with engine.connect() as conn:
        table_exists = engine.dialect.has_table(conn, table_name)
        assert table_exists

def test_table_names(engine, test_stream):
    with engine.connect() as conn:
        tables = engine.dialect.get_table_names(conn)
        assert "test_stream" in tables

def test_view_names(test_environment, engine, test_stream):
    view_name = "example_mv"
    view = View(env=test_environment).name(view_name)

    try:
        view.delete()
    except Exception:
        pass

    view = (
        View(env=test_environment)
        .name(view_name)
        .query("select * from test_stream")
        .create()
    )

    time.sleep(1)

    with engine.connect() as conn:
        views = engine.dialect.get_view_names(conn)
        print(views)
        assert "example_mv" in views

    view.delete()

def test_materialized_view_names(engine,test_environment,test_stream):
    view_name = "example_mv"
    view = View(env=test_environment).name(view_name)

    try:
        view.delete()
    except Exception:
        pass

    view = (
        View(env=test_environment)
        .name(view_name)
        .query("select * from test_stream")
        .materialized(True)
        .create()
    )

    with engine.connect() as conn:
        mvs = engine.dialect.get_materialized_view_names(conn)
        assert "example_mv" in mvs

    view.delete()

def test_view_reflection(test_environment, engine, test_stream):
    view_name = "test_view"
    view = View(env=test_environment).name(view_name)

    try:
        view.delete()
    except Exception:
        pass

    view = (
        View(env=test_environment)
        .name(view_name)
        .query("select * from test_stream")
        .create()
    )

    time.sleep(1)
    metadata_obj = MetaData()
    test_view = Table("test_view", metadata_obj, autoload_with=engine)
    assert test_view is not None
    column_names = [c.name for c in test_view.columns]
    assert "time" in column_names
    assert "data" in column_names

    view.delete()
    time.sleep(3)

def test_table_reflection(engine, test_stream):
    metadata_obj = MetaData()
    test_table = Table("test_stream", metadata_obj, autoload_with=engine)
    assert test_table is not None
    column_names = [c.name for c in test_table.columns]
    assert "time" in column_names
    assert "data" in column_names

def test_select_query(engine, test_stream):
    metadata_obj = MetaData()
    test_table = Table("test_stream", metadata_obj, autoload_with=engine)
    one_hour_ago = text("now() - 1h")
    stmt = select(test_table).where(
        test_table.c._tp_time > one_hour_ago,
        test_table.c.time > 1
    )
    compiled_query = stmt.compile(compile_kwargs={"literal_binds": True})
    print(f"compiled_query {compiled_query}")

    with engine.connect() as conn:
        count = 0
        max = 2
        for row in conn.execute(stmt):
            assert row is not None
            count += 1
            if count >= max:
                break
        assert count == max
