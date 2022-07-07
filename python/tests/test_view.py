from timeplus import View


def test_view(test_environment):
    view = View().name("testview").query("select * from clicks").materialized(False)
    view.create()

    view_names = [v.name() for v in View.list()]
    assert view.name() in view_names

    view.delete()

    view_names = [v.name() for v in View.list()]
    assert view.name() not in view_names
