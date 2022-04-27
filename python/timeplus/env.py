"""
env

This module defines environment class  
:copyright: (c) 2022 by Timeplus  
:license: Apache2, see LICENSE for more details.  
"""

import sys
import os
import requests
from requests.structures import CaseInsensitiveDict

from timeplus.base import Base
from timeplus.error import TimeplusAPIError
from loguru import logger

log_level = os.environ.get("GLUON_LOG_LEVEL", "INFO")

logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    format="{time} - {level} - {message}",
    level=log_level,
)
logger.add("gluon.log", rotation="500 MB", level=log_level)


class Env(Base):
    """
    Env class defines running environment of Timeplus.
    """

    _envs = None
    _current_env = None

    def __init__(self):
        Base.__init__(self)
        self.host("localhost")
        self.port("8000")
        self.schema("http")
        self.prop("token", "")

        self._headers = CaseInsensitiveDict()
        self._headers["Accept"] = "application/json"
        self._headers["Content-Type"] = "application/json"
        self._headers["Timeplus-Request-From"] = "gluon"
        self._http_timeout = 10

        Env.add(self)
        self._logger = logger

    @classmethod
    def add(cls, env):
        if cls._envs is None:
            cls._envs = []

        cls._envs.append(env)

        if len(cls._envs) == 1:
            cls._current_env = env

    @classmethod
    def current(cls):
        return cls._current_env

    @classmethod
    def setCurrent(cls, env):
        cls._current_env = env

    @classmethod
    def envs(cls):
        return cls._envs

    def host(self, *args):
        return self.prop("host", *args)

    def port(self, *args):
        return self.prop("port", *args)

    def schema(self, *args):
        return self.prop("schema", *args)

    def base_url(self):
        return f"{self.schema()}://{self.host()}:{self.port()}/api/v1beta1"

    def headers(self):
        self._headers["Authorization"] = f"Bearer {self.token()}"
        return self._headers

    def token(self, *args):
        return self.prop("token", *args)

    def info(self):
        url = f"{self.schema()}://{self.host()}:{self.port()}/info"
        try:
            r = requests.get(url, timeout=self.http_timeout())
            if r.status_code < 200 or r.status_code > 299:
                err_msg = f"failed to show info due to {r.text}"
                self._logger.error(err_msg)
                raise TimeplusAPIError("get", r.status_code, err_msg)
            else:
                return r.json()
        except Exception as e:
            raise e

    def ping(self):
        url = f"{self.schema()}://{self.host()}:{self.port()}/health"
        try:
            r = requests.get(url, timeout=self.http_timeout())
            if r.status_code < 200 or r.status_code > 299:
                err_msg = f"failed to ping due to {r.text}"
                self._logger.error(err_msg)
                raise TimeplusAPIError("get", r.status_code, err_msg)
            else:
                return r.json()
        except Exception as e:
            raise e

    def logger(self):
        return self._logger

    def http_timeout(self):
        return self._http_timeout
