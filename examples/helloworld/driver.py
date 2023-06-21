import os
from sqlalchemy import create_engine, text, MetaData, Table
from sqlalchemy.dialects import registry

registry.register("timeplus", "timeplus.sqlalchemy", "TimeplusDialect")

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = "dev.timeplus.cloud"
port = 443
workspace = os.environ.get("TIMEPLUS_WORKSPACE") or "tp-demo"

engine = create_engine(f"timeplus://:{api_key}@{api_address}:{port}/{workspace}")

table_name = "car_live_data"


# check stream existense
with engine.connect() as conn:
    table_exists = engine.dialect.has_table(conn, table_name)
    print(f"{table_name} exist : {table_exists}")


# stream/table refection
metadata_obj = MetaData()
car_table = Table(table_name, metadata_obj, autoload_with=engine)
print(f"reflected table is {car_table}")
print(f"cols is {[ (c.name, c.type) for c in car_table.columns]}")

# execute driver sql
with engine.connect() as conn:
    result = conn.exec_driver_sql("select * from table(car_live_data) limit 5")
    for row in result:
        print(f"got one row {row}")

# execute text sql
with engine.connect() as connection:
    result = connection.execute(text("select * from table(car_live_data) limit 5"))
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
