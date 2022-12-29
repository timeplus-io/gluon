"""
conftest.py
"""
import pytest
import os

from timeplus import Environment


@pytest.fixture
def test_environment():
    api_key = os.environ.get("TIMEPLUS_API_KEY")
    api_address = os.environ.get("TIMEPLUS_HOST")
    worksapce = os.environ.get("TIMEPLUS_WORKSPACE")

    return Environment().address(api_address).apikey(api_key).workspace(worksapce)
