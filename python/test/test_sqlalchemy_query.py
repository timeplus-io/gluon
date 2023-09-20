from sqlalchemy import text, select, MetaData, Table
from timeplus import View


def test_driver_sql(engine):
    with engine.connect() as conn:
        result = conn.exec_driver_sql(
            "select cid from table(car_live_data) limit 5")
        assert len(result.fetchall()) == 5


def test_driver_sql_live(engine):
    with engine.connect() as conn:
        result = conn.exec_driver_sql(
            "select cid from car_live_data limit 5")
        assert len(result.fetchall()) == 5


def test_text_sql(engine):
    with engine.connect() as connection:
        result = connection.execute(
            text("select * from table(car_live_data) limit 3"))
        rows = [row for row in result]
        assert len(rows) == 3


def test_text_sql_live(engine):
    with engine.connect() as connection:
        result = connection.execute(
            text("select * from car_live_data limit 3"))
        rows = [row for row in result]
        assert len(rows) == 3


def test_text_streaming_sql(engine):
    with engine.connect() as connection:
        result = connection.execute(text("select * from car_live_data"))
        count = 0
        max = 10
        for row in result:
            assert row is not None
            count += 1
            if count >= max:
                break
        assert count == max


def test_check_stream_existence(engine):
    table_name = "car_live_data"
    with engine.connect() as conn:
        table_exists = engine.dialect.has_table(conn, table_name)
        assert table_exists


def test_table_names(engine):
    with engine.connect() as conn:
        tables = engine.dialect.get_table_names(conn)
        assert "car_live_data" in tables


def test_view_names(engine):
    with engine.connect() as conn:
        views = engine.dialect.get_view_names(conn)
        print(views)
        assert "car_info" in views


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


def test_view_reflection(engine):
    metadata_obj = MetaData()
    car_view = Table("car_live_data", metadata_obj, autoload_with=engine)
    assert car_view is not None
    column_names = [c.name for c in car_view.columns]
    assert "speed_kmh" in column_names


def test_table_reflection(engine):
    metadata_obj = MetaData()
    car_table = Table("car_live_data", metadata_obj, autoload_with=engine)
    assert car_table is not None
    column_names = [c.name for c in car_table.columns]
    assert "cid" in column_names


def test_select_query(engine):
    metadata_obj = MetaData()
    car_table = Table("car_live_data", metadata_obj, autoload_with=engine)
    stmt = select(car_table).where(car_table.c.speed_kmh > 50)
    with engine.connect() as conn:
        count = 0
        max = 3
        for row in conn.execute(stmt):
            assert row is not None
            count += 1
            if count >= max:
                break
        assert count == max
