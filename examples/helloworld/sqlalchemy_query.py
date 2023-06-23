import os
from sqlalchemy import create_engine, text, select, MetaData, Table
from sqlalchemy.dialects import registry

registry.register("timeplus", "timeplus.sqlalchemy", "TimeplusDialect")

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = "dev.timeplus.cloud"
port = 443
workspace = os.environ.get("TIMEPLUS_WORKSPACE") or "tp-demo"

engine = create_engine(
    f"timeplus://:{api_key}@{api_address}:{port}/{workspace}")

# execute driver sql
with engine.connect() as conn:
    result = conn.exec_driver_sql(
        "select cid from table(car_live_data) limit 5")
    print(result.fetchall())

# execute text sql
with engine.connect() as connection:
    result = connection.execute(
        text("select * from table(car_live_data) limit 3"))
    for row in result:
        print(f"got one row : {row}")

# execute text streaming sql
with engine.connect() as connection:
    result = connection.execute(text("select * from car_live_data"))
    count = 0
    max = 10
    for row in result:
        print(f"got one row : {row}")
        count += 1
        if count >= max:
            break

# check stream existense
table_name = "car_live_data"
with engine.connect() as conn:
    table_exists = engine.dialect.has_table(conn, table_name)
    print(f"{table_name} exist : {table_exists}")

# list all tables
with engine.connect() as conn:
    tables = engine.dialect.get_table_names(conn)
    print(f"list tables : {tables}")

# list all views
with engine.connect() as conn:
    views = engine.dialect.get_view_names(conn)
    print(f"list views : {views}")

# list all mv
with engine.connect() as conn:
    mvs = engine.dialect.get_materialized_view_names(conn)
    print(f"list materialized views : {mvs}")

# view reflection
metadata_obj = MetaData()
slack_view = Table("slack_users", metadata_obj, autoload_with=engine)
print(f"reflected view is {slack_view}")
print(f"cols is {[ (c.name, c.type) for c in slack_view.columns]}")

# stream/table reflection
metadata_obj = MetaData()
car_table = Table(table_name, metadata_obj, autoload_with=engine)
print(f"reflected table is {car_table}")
print(f"cols is {[ (c.name, c.type) for c in car_table.columns]}")

stmt = select(car_table).where(car_table.c.cid == "c00001")
print(stmt)
with engine.connect() as conn:
    count = 0
    max = 3
    for row in conn.execute(stmt):
        print(f"got one row from query {row}")
        count += 1
        if count >= max:
            break
