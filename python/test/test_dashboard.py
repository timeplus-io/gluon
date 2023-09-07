from timeplus import Dashboard


def test_dashboard(test_environment):
    Dashboard(env=test_environment).list()
