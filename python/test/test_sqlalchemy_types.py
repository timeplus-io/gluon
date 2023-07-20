from sqlalchemy import text


def test_select_basic_types(engine):
    with engine.connect() as conn:
        result = conn.execute(text(
            "select 1, 1.5, 'abc' , true, false, today(), now(), now64(), 1=2, 1<>2, uuid()"))
        for row in result:
            assert len(row) == 11


def test_select_composite_array_tuple(engine):
    with engine.connect() as conn:
        result = conn.execute(text(
            "select [1,2,3], (1, 'abc', 1.2)"))
        for row in result:
            assert len(row) == 2
            assert len(row[0]) == 3
            assert len(row[1]) == 3


def test_select_composite_map(engine):
    with engine.connect() as conn:
        result = conn.execute(text(
            "SELECT cast(([1, 2, 3], ['a', 'b', 'c']), 'map(int, string)') AS map"))
        for row in result:
            assert len(row) == 1
            assert len(row[0]) == 3
            assert set(row[0].keys()) == {'1', '2', '3'}
            assert set(row[0].values()) == {'a', 'b', 'c'}
