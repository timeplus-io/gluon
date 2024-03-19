from timeplus import Topology


def test_topology(test_environment):
    topology = Topology(env=test_environment).get()

    assert topology is not None
