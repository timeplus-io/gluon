import pytest
from timeplus import Alert

#@pytest.mark.skip(reason="alert api has validation issue")
def test_alert(test_environment):
    Alert(env=test_environment).list()
