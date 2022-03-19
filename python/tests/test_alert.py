import time
from timeplus import Alert, SlackSinkProperty


def test_alerts(local_environment):
    alerts = Alert.list()
    assert alerts is not None

    alert = Alert().name("test alert").type("slack").rule("select * from iot")
    prop = (SlackSinkProperty()
        .url(
            "https://hooks.slack.com/services/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"
        )
        .message(
            "You have a new alert hostnamet {{.hostname}}:\n*<fakeLink.timeplus.com|Gang Tao - New Alert>*"
        ))
    alert.properties(prop)
    alert.create()

    assert alert.get().data() is not None

    time.sleep(3)
    alert.delete()
