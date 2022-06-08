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
        self.api_version("api/v1beta1")
        self.token("")
        self.domain = "timeplus.us.auth0.com"
        self._max_token_refresh = 24
        self._token_refresh = 0

        self._headers = CaseInsensitiveDict()
        self._headers["Accept"] = "application/json"
        self._headers["Content-Type"] = "application/json"
        self._headers["Timeplus-Request-From"] = "gluon"
        self._headers["Connection"] = "close"

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

    def audience(self, *args):
        return self.prop("audience", *args)

    def client_id(self, *args):
        return self.prop("client_id", *args)

    def client_secret(self, *args):
        return self.prop("client_secret", *args)

    def api_version(self, *args):
        return self.prop("api_version", *args)

    def base_url(self):
        return f"{self.schema()}://{self.host()}:{self.port()}/{self.api_version()}"

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

    def request_token(self):
        url = f"https://{self.domain}/oauth/token"
        self.logger().debug(f"request token from {url}")

        try:
            data = {
                "client_id": self.client_id(),
                "client_secret": self.client_secret(),
                "audience": self.audience(),
                "grant_type": "client_credentials",
            }
            self.logger().debug(f"request token data {data}")
            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/json"
            r = requests.post(url, json=data, headers=headers)
            if r.status_code < 200 or r.status_code > 299:
                err_msg = f"failed to request code due to {r.text}"
                self._logger.error(err_msg)
                raise TimeplusAPIError("post", r.status_code, err_msg)
            else:
                return r.json()
        except Exception as e:
            raise e

    def refresh_token(self):
        self._logger.info(f"refresh token {self._token_refresh}")
        token = self.request_token()
        self.token(token["access_token"])
        self._logger.info(f"set token to {self.token()}")
        self._token_refresh += 1
        if self._token_refresh > self._max_token_refresh:
            raise TimeplusAPIError("token_refresh", 0, "max refresh reached")

        return self

    def logger(self):
        return self._logger

    def http_timeout(self):
        return self._http_timeout

    def http_post(self, url, data):
        self.logger().debug("post url {} with data {}", url, data)
        try:
            with requests.Session() as session:
                r = session.post(
                    url,
                    json=data,
                    headers=self.headers(),
                    timeout=self.http_timeout(),
                )
                if r.status_code < 200 or r.status_code > 299:
                    err_msg = f"failed to send http post due to {r.text}"
                    if r.status_code == 401:
                        self.refresh_token()
                        return self.http_post(url, data)
                    else:
                        raise TimeplusAPIError("post", r.status_code, err_msg)
                else:
                    return r
        except Exception as e:
            self._logger.error(f"http post failed {e}")
            raise e

    def http_post_data(self, url, data):
        self.logger().debug("post {} with data {}", url, data)
        try:
            with requests.Session() as session:
                r = session.post(
                    url,
                    data=data,
                    headers=self.headers(),
                    timeout=self.http_timeout(),
                )
                if r.status_code < 200 or r.status_code > 299:
                    err_msg = f"failed to send http post due to {r.text}"
                    if r.status_code == 401:
                        self.refresh_token()
                        return self.http_post_data(url, data)
                    else:
                        raise TimeplusAPIError("post", r.status_code, err_msg)
                else:
                    return r
        except Exception as e:
            self._logger.error(f"http post failed {e}")
            raise e

    def http_get(self, url):
        self.logger().debug("get {}", url)
        try:
            with requests.Session() as session:
                r = session.get(
                    url,
                    headers=self.headers(),
                    timeout=self.http_timeout(),
                )
                if r.status_code < 200 or r.status_code > 299:
                    err_msg = f"failed to send http get due to {r.text}"
                    if r.status_code == 401:
                        self.refresh_token()
                        return self.http_get(url)
                    else:
                        raise TimeplusAPIError("get", r.status_code, err_msg)
                else:
                    return r.json()
        except Exception as e:
            self.logger().error(f"http get failed {e}")
            raise e

    def http_delete(self, url):
        self.logger().debug("delete {}", url)
        try:
            with requests.Session() as session:
                r = session.delete(
                    url,
                    headers=self.headers(),
                    timeout=self.http_timeout(),
                )
                if r.status_code < 200 or r.status_code > 299:
                    err_msg = f"failed to send httpdelete due to {r.text}"
                    self._logger.error(err_msg)

                    if r.status_code == 401:
                        self.refresh_token()
                        return self.http_delete(url)
                    else:
                        raise TimeplusAPIError("delete", r.status_code, err_msg)
                else:
                    return
        except Exception as e:
            self._logger.error(f"delete failed {e}")
            raise e
