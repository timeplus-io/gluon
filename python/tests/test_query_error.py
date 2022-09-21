import pytest
from rx import operators as ops
from timeplus import Query


def test_query(test_environment):
    query = Query().name("ad hoc query").sql("select * from iot")
    query.create()

    result = []
    errors = []
    query.get_result_stream().subscribe(
        on_next=lambda i: result.append(i),
        on_error=lambda e: errors.append(e),
        on_completed=lambda: query.stop(),
    )

    assert len(errors) == 0
    query.delete()
