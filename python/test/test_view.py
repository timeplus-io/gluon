from timeplus import View
from timeplus.error import TimeplusAPIError


def test_view(test_environment, test_table):
    view_list = View(env=test_environment).list()
    initial_count = len(view_list)

    view_name = "test_view"

    # Create a new view
    view = (
        View(env=test_environment)
        .name(view_name)
        .query("select * from test_table")
        .create()
    )

    view_list = View(env=test_environment).list()
    new_count = len(view_list)

    assert new_count == initial_count + 1

    # Clean up: delete the created view
    view.delete()
    view_list = View(env=test_environment).list()
    final_count = len(view_list)

    assert final_count == initial_count


def test_materialized_view(test_environment, test_table):
    view_name = "test_materialized_view"

    # Create a new materialized view
    view = (
        View(env=test_environment)
        .name(view_name)
        .query("select * from test_table")
        .materialized(True)
        .create()
    )

    # Check that the view was created
    assert view.exist() == True

    # Clean up: delete the created view
    view.delete()


def test_view_description(test_environment, test_table):
    view_name = "test_view_description"

    # Create a new view with a description
    view = (
        View(env=test_environment)
        .name(view_name)
        .query("select * from test_table")
        .description("This is a test view")
        .create()
    )

    # Check that the view was created and description is correct
    assert view.exist() == True
    assert view.metadata().description == "This is a test view"

    # Clean up: delete the created view
    view.delete()


def test_view_target_stream(test_environment, test_table):
    view_name = "test_view_target_stream"
    target_stream_name = "test_target_stream"

    # Create a new view with a target stream
    view = (
        View(env=test_environment)
        .name(view_name)
        .query("select * from test_table")
        .target_stream(target_stream_name)
        .create()
    )

    # Check that the view was created and target stream is correct
    assert view.exist() == True
    assert view.metadata().target_stream == target_stream_name

    # Clean up: delete the created view
    view.delete()


def test_delete_nonexistent_view(test_environment):
    view_name = "nonexistent_view"
    view = View(env=test_environment).name(view_name)

    # Attempt to delete a view that doesn't exist
    try:
        view.delete()
        assert False, "Expected an error when trying to delete a nonexistent view"
    except TimeplusAPIError:
        pass  # Expected

