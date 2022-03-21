import requests

from timeplus.base import Base
from timeplus.env import Env


class ResourceBase(Base):
    _resource_name = "resource"

    def __init__(self, env=None):
        Base.__init__(self)
        if env is None:
            env = Env.current()
        self._headers = env.headers()
        self._base_url = env.base_url()
        self._env = env

    def create(self):
        url = f"{self._base_url}/{self._resource_name}/"
        print(f"post {url}")
        try:
            r = requests.post(
                f"{self._base_url}/{self._resource_name}/",
                json=self.data(),
                headers=self._headers,
            )
            if r.status_code < 200 or r.status_code > 299:
                print(
                    f"failed to create {self._resource_name} {r.status_code } {r.text}"
                )
            else:
                print(f"source {self._resource_name} has been created")
                self._data = r.json()
        except Exception as e:
            print(f"failed to create {self._resource_name} {e}")
        finally:
            return self

    def get(self):
        print(f"get {self._base_url}/{self._resource_name}/")
        try:
            r = requests.get(
                f"{self._base_url}/{self._resource_name}/{self.id()}",
                headers=self._headers,
            )
            if r.status_code < 200 or r.status_code > 299:
                print(f"failed to get {self._resource_name} {r.text}")
            else:
                print(f"get {self._resource_name} success")
                self._data = r.json()
        except Exception as e:
            print(f"failed to get {self._resource_name} {e}")
        finally:
            return self

    def delete(self):
        print(f"delete {self._base_url}/{self._resource_name}/{self.id()}")
        try:
            r = requests.delete(
                f"{self._base_url}/{self._resource_name}/{self.id()}",
                headers=self._headers,
            )
            if r.status_code < 200 or r.status_code > 299:
                print(
                    f"failed to delete {self._resource_name} {r.status_code} {r.text}"
                )
            else:
                print(f"delete {self._resource_name} success")
        except Exception as e:
            print(f"failed to delete {self._resource_name} {e}")
        finally:
            return self

    def action(self, action_name):
        print(f"post {self._base_url}/{self._resource_name}/{self.id()}/{action_name}")
        try:
            r = requests.post(
                f"{self._base_url}/{self._resource_name}/{self.id()}/{action_name}",
                headers=self._headers,
            )
            if r.status_code < 200 or r.status_code > 299:
                print(f"failed to post {action_name} on {self._resource_name} {r.text}")
            else:
                print(f"{action_name} {self._resource_name} success")
        except Exception as e:
            print(f"failed to {action_name} {self._resource_name} {e}")
        finally:
            return self

    @classmethod
    def list(cls, env=None):
        if env is None:
            env = Env.current()
        headers = env.headers()
        base_url = env.base_url()

        try:
            url = f"{base_url}/{cls._resource_name}/"
            r = requests.get(url, headers=headers)
            if r.status_code < 200 or r.status_code > 299:
                print(f"failed to list {cls._resource_name} {r.text}")
            else:
                print(f"list {cls._resource_name} success")
                result = [cls.build(val, env=env) for val in r.json()]
                return result
        except Exception as e:
            print(f"failed to list {cls._resource_name}")
