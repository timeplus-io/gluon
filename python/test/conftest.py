"""
conftest.py
"""

import pytest
import os
import time
from urllib.parse import urlparse
from timeplus.dbapi import connect

from timeplus import Environment
from timeplus import Stream
from timeplus.error import TimeplusAPIError
from sqlalchemy import create_engine, text, select, MetaData, Table
from sqlalchemy.dialects import registry

registry.register("timeplus", "timeplus.sqlalchemy", "TimeplusDialect")

@pytest.fixture
def test_environment():
    api_key = os.environ.get("TIMEPLUS_API_KEY")
    api_address = os.environ.get("TIMEPLUS_HOST")
    workspace = os.environ.get("TIMEPLUS_WORKSPACE")
    username = os.environ.get("TIMEPLUS_USERNAME")
    password = os.environ.get("TIMEPLUS_PASSWORD")

    print(f"api address:{api_address}, workspace:{workspace}")

    env = Environment().address(api_address).workspace(workspace)

    if api_key is not None:
        env.apikey(api_key)
    
    if username is not None:
        env.username(username)

    if password is not None:
        env.password(password)

    return env


@pytest.fixture
def test_stream(test_environment):
    stream_name = "test_stream"

    # Create a new stream instance with the given name
    stream = Stream(env=test_environment).name(stream_name)

    try:
        stream.delete()
        time.sleep(3)
    except Exception:
        pass

    time.sleep(3)

    replication_number = os.environ.get("TIMEPLUS_REPLICATION_NUMBER")

    # Create a new stream
    stream = (
        Stream(env=test_environment)
        .name(stream_name)
        .column("time", "integer")
        .column("data", "string")
        .replication_factor(int(replication_number))
        .shards(3)
        .create()
    )

    time.sleep(3)

    value = [["time", "data"], [[0, "abcd"]]]
    stream.ingest(*value)
    # Provide the stream to the test
    return stream


@pytest.fixture
def engine():
    api_key = os.environ.get("TIMEPLUS_API_KEY")
    username = os.environ.get("TIMEPLUS_USERNAME")
    password = os.environ.get("TIMEPLUS_PASSWORD")
    api_address = os.environ.get("TIMEPLUS_HOST")
    parsed_url = urlparse(api_address)
    api_netloc = parsed_url.netloc
    api_schema = parsed_url.scheme

    workspace = os.environ.get("TIMEPLUS_WORKSPACE") or "tp-demo"

    if api_key is not None:
        engine_connection_string = f"timeplus://:{api_key}@{api_netloc}/{workspace}"
        print(f"create engine with connection {engine_connection_string}")
        engine = create_engine(engine_connection_string)
        return engine
    else:
        engine = create_engine(
            f"timeplus://{username}:{password}@{api_netloc}/{workspace}")

        return engine


@pytest.fixture
def conn():
    api_key = os.environ.get("TIMEPLUS_API_KEY")
    username = os.environ.get("TIMEPLUS_USERNAME")
    password = os.environ.get("TIMEPLUS_PASSWORD")
    api_address = os.environ.get("TIMEPLUS_HOST")
    parsed_url = urlparse(api_address)

    schema = parsed_url.scheme
    host = parsed_url.hostname
    port = parsed_url.port

    if schema == "https" and port is None:
        port = 443

    if schema == "http" and port is None:
        port = 80

    api_address = "dev.timeplus.cloud"
    workspace = os.environ.get("TIMEPLUS_WORKSPACE")

    if api_key is not None:
        conn = connect(host=host, port=port, scheme=schema, password=api_key, path=workspace)
        return conn
    else:
        conn = connect(host=host, port=port, scheme=schema, user= username, password=password, path=workspace)
        return conn