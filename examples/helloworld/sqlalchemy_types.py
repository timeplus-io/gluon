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
    result = conn.execute(text(
        "select 1, 1,0, 'abc' , true, false, now(), 1=2, uuid()"))
    for row in result:
        print(row)
