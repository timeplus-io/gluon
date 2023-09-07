from timeplus import Alert


def test_alert(test_environment):
    Alert(env=test_environment).list()
