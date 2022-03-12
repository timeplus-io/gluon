from timeplus import Stream


def test_stream():
    for s in Stream.list():
        print(s.name())
