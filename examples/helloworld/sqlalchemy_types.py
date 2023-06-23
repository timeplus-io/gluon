import os
from sqlalchemy import create_engine, text
from sqlalchemy.dialects import registry

registry.register("timeplus", "timeplus.sqlalchemy", "TimeplusDialect")

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = "dev.timeplus.cloud"
port = 443
workspace = os.environ.get("TIMEPLUS_WORKSPACE") or "tp-demo"

engine = create_engine(
    f"timeplus://:{api_key}@{api_address}:{port}/{workspace}")

# select basic types
with engine.connect() as conn:
    result = conn.execute(text(
        "select 1, 1.5, 'abc' , true, false, today(), now(), now64(), 1=2, 1<>2, uuid()"))
    for row in result:
        print(row)

# select compsite types : array, tuple
with engine.connect() as conn:
    result = conn.execute(text(
        "select [1,2,3], (1, 'abc', 1.2)"))
    for row in result:
        print(row)

# select compsite types : map
with engine.connect() as conn:
    result = conn.execute(text(
        "SELECT cast(([1, 2, 3], ['a', 'b', 'c']), 'map(int, string)') AS map"))
    for row in result:
        print(row)
