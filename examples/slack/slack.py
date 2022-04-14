import os
import websocket
import json
import rel
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime

from timeplus import Env, Stream, StreamColumn


def staging_environment():
    client_id = os.environ.get("AUTH0_API_CLIENT_ID")
    client_secret = os.environ.get("AUTH0_API_CLIENT_SECRET")
    env = (
        Env()
        .schema("https")
        .host("staging.demo.timeplus.io")
        .port("443")
        .login(client_id=client_id, client_secret=client_secret)
    )
    Env.setCurrent(env)
    return env


class SlackSource:
    def __init__(self, token):
        self.token = token
        self.url = "https://slack.com/api/rtm.connect"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = f"Bearer {self.token}"
        self.headers = headers
        self.wsurl = None
        self.init_stream()

    def init_stream(self):
        self.event_stream = (
            Stream()
            .name("timeplus_slack_events")
            .column(StreamColumn().name("message").type("string"))
            .column(StreamColumn().name("time").type("datetime64(3)"))
        )

        if self.event_stream.get() is None:
            try:
                self.event_stream.create()
            except Exception as e:
                print(f"failed to create stream {e}")

        self.user_stream = (
            Stream()
            .name("timeplus_slack_users")
            .column(StreamColumn().name("id").type("string"))
            .column(StreamColumn().name("name").type("string"))
        )

        if self.user_stream.get() is None:
            try:
                self.user_stream.create()
            except Exception as e:
                print(f"failed to create stream {e}")

    def get_user(self, id):
        user_info_url = f"https://slack.com/api/users.info?user={id}"
        resp = requests.get(user_info_url, headers=self.headers)

        if resp.status_code == 200:
            print("get user info success")
            try:
                user_info = resp.json()
                self.user_stream.insert([[id, user_info["user"]["real_name"]]])
            except Exception as e:
                print(f"failed to insert stream {e}")

    def connect(self):
        resp = requests.get(self.url, headers=self.headers)
        if resp.status_code == 200:
            print("connecting success")
            print(resp.json())
            self.wsurl = resp.json()["url"]
        else:
            raise Exception("failed to connect")

        ws = websocket.WebSocketApp(
            self.wsurl,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )

        ws.run_forever(dispatcher=rel)
        rel.signal(2, rel.abort)  # Keyboard Interrupt
        rel.dispatch()

    def on_message(self, ws, message):
        print(message)
        event = json.loads(message)

        if event["type"] == "message":
            self.get_user(event["user"])
        self.event_stream.insert(
            [
                [
                    message,
                    datetime.now(),
                ]
            ]
        )

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print("### closed ###")

    def on_open(self, ws):
        print("Opened connection")


token = os.environ.get("SLACK_BOT_TOKEN")
env = staging_environment()
slack = SlackSource(token)
slack.connect()
