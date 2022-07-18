import pytest
import time

from timeplus import Metrics


def test_new_metrics(test_environment):
    m = Metrics("pytest")
    try:
        m.delete()
    except Exception as e:
        test_environment._logger.warning(f"failed to delete metrics {e}")

    m = Metrics("pytest", True, ["value"], ["a", "b", "c"])
    m.start()
    m.observe("timeplus", "pytest", [1.1], ["x", "xxx", "xx"], None)

    with pytest.raises(Exception):
        m.observe("timeplus", "pytest", [1.1, 1.2], ["x", "xxx", "xx"], None)

    with pytest.raises(Exception):
        m.observe("timeplus", "pytest", [1.1], ["x"], None)

    time.sleep(3)
    m.stop()


def test_get_metrics(test_environment):
    m = Metrics("pytest")
    try:
        m.delete()
    except Exception as e:
        test_environment._logger.warning(f"failed to delete metrics {e}")

    m = Metrics("pytest", True, ["value"], ["a", "b", "c"])
    m = Metrics("pytest")
    m.start()

    m.observe("timeplus", "pytest", [1.1], ["x", "xxx", "xx"], None)
    with pytest.raises(Exception):
        m.observe("timeplus", "pytest", [1.1, 1.2], ["x", "xxx", "xx"], None)

    with pytest.raises(Exception):
        m.observe("timeplus", "pytest", [1.1], ["x"], None)

    time.sleep(3)
    m.stop()
