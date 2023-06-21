import os
from sqlalchemy import create_engine, text
from sqlalchemy.dialects import registry

registry.register("timeplus", "timeplus.sqlalchemy", "TimeplusDialect")

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = "dev.timeplus.cloud"
port = 443
workspace = os.environ.get("TIMEPLUS_WORKSPACE")

engine = create_engine(f"timeplus://:{api_key}@{api_address}:{port}/{workspace}")

print(engine)

with engine.connect() as connection:
    result = connection.execute(text("select * from car_live_data"))
    print(result)
    for row in result:
        print(f"row : {row}")
