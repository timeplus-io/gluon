import time
from rx import operators as ops

from timeplus import (
    GeneratorConfiguration,
    GeneratorField,
    GeneratorSource,
    SourceConnection,
    Query,
    Source,
    Stream,
)


def test_query(staging_environment):
    query = (
        Query()
        .name("ad hoc query")
        .sql(
            "select time, gas_percent, speed_kmh from car_live_data where cid='c00004'"
        )
    )
    query.create()

    result = []
    query.get_result_stream().pipe(ops.take(5)).subscribe(
        on_next=lambda i: result.append(i),
        on_error=lambda e: print(f"error {e}"),
        on_completed=lambda: query.stop(),
    )

    assert len(result) == 5
    query.delete()


def test_sync_query(staging_environment):
    result = Query.execSQL("select * from table(car_live_data) limit 2")
    assert result is not None
