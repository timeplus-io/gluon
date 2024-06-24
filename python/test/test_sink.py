import pytest
from timeplus import Sink

@pytest.mark.skipif(reason="Skipping this test due to kafka sink move to external stream")
def test_sink_kafka(test_environment):
    sink_name = "test_kafka_sink"

    sink_type = "kafka"
    sink_query = "select * from car_live_data"
    sink_properties = {
        "brokers": "kafka.user-gang:9092",
        "topic": "test_car_live_data",
        "tls": {
            "disable": True,
            "skip_verify_server": True
        }
    }
    sink_description = ""
    sink = (
        Sink(env=test_environment)
        .name(sink_name)
        .type(sink_type)
        .query(sink_query)
        .properties(sink_properties)
        .description(sink_description)
        .create()
    )

    sink_list = Sink(env=test_environment).list()
    sink_id = sink.id()
    assert sink_name in [q.name for q in sink_list]

    assert Sink(env=test_environment).id(sink_id).exist()

    sink.delete()

    sink_list = Sink(env=test_environment).list()
    assert sink_name not in [s.name for s in sink_list]

    assert not Sink(env=test_environment).id(sink_id).exist()
