"""
resource

This module defines base class for REST resource class  
:copyright: (c) 2022 by Timeplus  
:license: Apache2, see LICENSE for more details.  
"""

import requests

from timeplus.base import Base
from timeplus.env import Env
from timeplus.error import TimeplusAPIError


class ResourceBase(Base):
    """
    ResourceBase class defines base class for all REST resoruce objects
    """

    _resource_name = "resource"

    def __init__(self, env=None):
        Base.__init__(self)
        if env is None:
            env = Env.current()
        self._headers = env.headers()
        self._base_url = env.base_url()
        self._env = env
        self._logger = env.logger()

    def create(self):
        url = f"{self._base_url}/{self._resource_name}/"
        try:
            result = self._env.http_post(url, self.data())
            self._data = result.json()
            return self
        except Exception as e:
            self._logger.error(f"create failed {e}")
            raise e

    def get(self):
        url = f"{self._base_url}/{self._resource_name}/{self.id()}"
        try:
            result = self._env.http_get(url)
            self._data = result
            return self
        except Exception as e:
            raise e

    def delete(self):
        url = f"{self._base_url}/{self._resource_name}/{self.id()}"
        try:
            self._env.http_delete(url)
            return self
        except Exception as e:
            raise e

    def action(self, action_name):
        url = f"{self._base_url}/{self._resource_name}/{self.id()}/{action_name}"
        try:
            self._env.http_post(url, None)
            return self
        except Exception as e:
            self._logger.error(f"action failed {e}")
            raise e

    @classmethod
    def list(cls, env=None):
        if env is None:
            env = Env.current()
        url = f"{env.base_url()}/{cls._resource_name}/"

        try:
            get_result = env.http_get(url)
            result = [cls.build(val, env=env) for val in get_result]
            return result
        except Exception as e:
            raise e
