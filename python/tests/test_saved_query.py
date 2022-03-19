import time
from timeplus import SavedQuery


def test_saved_query(local_environment):
    querys = SavedQuery.list()
    assert querys is not None

    query = SavedQuery().name("test").sql("select * from iot").description("test desc").tags(["a","b"])
    query.create()

    assert query.get().data() is not None
    query.delete()
