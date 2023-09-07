from timeplus import View


def test_view(test_environment, test_stream):
    view_list = View(env=test_environment).list()

    view_name = "test_view"

    # Create a new view
    view = (
        View(env=test_environment)
        .name(view_name)
        .query("select * from test_stream")
        .create()
    )

    view_list = View(env=test_environment).list()
    assert view_name in [q.name for q in view_list]

    get_view = View(env=test_environment).name(view_name).get()
    assert get_view.metadata().name == view_name


    # Clean up: delete the created view
    view.delete()

    view_list = View(env=test_environment).list()
    assert view_name not in [q.name for q in view_list]


def test_materialized_view(test_environment, test_stream):
    view_name = "test_materialized_view"

    # Create a new materialized view
    view = (
        View(env=test_environment)
        .name(view_name)
        .query("select * from test_stream")
        .materialized(True)
        .create()
    )

    # Check that the view was created
    assert view.exist()

    # Clean up: delete the created view
    view.delete()


def test_view_description(test_environment, test_stream):
    view_name = "test_view_description"

    # Create a new view with a description
    view = (
        View(env=test_environment)
        .name(view_name)
        .query("select * from test_stream")
        .description("This is a test view")
        .create()
    )

    # Check that the view was created and description is correct
    assert view.exist()
    assert view.metadata().description == "This is a test view"

    # Clean up: delete the created view
    view.delete()


def test_view_target_stream(test_environment, test_stream):
    view_name = "test_view_target_stream"
    target_stream_name = "test_target_stream"

    # Create a new view with a target stream
    view = (
        View(env=test_environment)
        .name(view_name)
        .query("select * from test_stream")
        .target_stream(target_stream_name)
        .create()
    )

    # Check that the view was created and target stream is correct
    assert view.exist() == True
    assert view.metadata().target_stream == target_stream_name

    # Clean up: delete the created view
    view.delete()


