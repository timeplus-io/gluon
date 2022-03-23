import streamlit as st

import os
import json
from datetime import datetime

import pandas as pd
import altair as alt

from river import compose
from river import linear_model
from river import metrics
from river import preprocessing

from timeplus import (
    Query,
    Env,
    Stopper,
)

from rx import operators as ops

st.title("Timeplus Platform")
st.write("Fast + powerful real-time analytics made intuitive.")
st.write("See https://timeplus.com")

# Environment
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
# st.write(env.info())

# Get Data from Car live data
query = (
    Query()
    .name("car query")
    .sql("select time, gas_percent, speed_kmh from car_live_data where cid='c00004'")
    .create()
)
stopper = Stopper()
result = []

if "model" not in st.session_state:
    model = compose.Pipeline(
        preprocessing.StandardScaler(), linear_model.LinearRegression()
    )
    metric = metrics.MAE()
    st.session_state["model"] = model
    st.session_state["metric"] = metric


def to_timestamp(dt):
    try:
        time = datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%fZ").timestamp()
        return time
    except Exception:
        time = datetime.strptime(dt, "%Y-%m-%dT%H:%M:%SZ").timestamp()
        return time


def handle_result(result):
    model = st.session_state["model"]
    metric = st.session_state["metric"]

    data = json.loads(result)
    time = to_timestamp(data[0])
    value = data[1]
    x = {"time": time}
    y = float(value)
    try:
        # st.write(f"predict one x={x},y ={y}")
        y_pred = model.predict_one(x)
        # st.write(f"predict one result {y_pred}")
        metric = metric.update(y, y_pred)
        # st.write(f"metric is {metric}")
        model = model.learn_one(x, y)

        col = ["time", "value", "prediction"]
        row_original = [time, y, "raw"]
        row_predict = [time, y_pred, "predict"]
        row_metrics = [time, metric.get(), "metric"]
        df = pd.DataFrame([row_original, row_predict, row_metrics], columns=col)

        if "chart" not in st.session_state:
            # query_result_table = st.table(df)
            # st.session_state["table"] = query_result_table
            # my_chart = st.line_chart(df)
            c = (
                alt.Chart(df)
                .mark_line()
                .encode(
                    x="time",
                    y="value",
                    color="prediction",
                )
            )
            my_chart = st.altair_chart(c, use_container_width=True)
            st.session_state["chart"] = my_chart
        else:
            st.session_state["chart"].add_rows(df)

    except Exception as e:
        st.write(f"failed to predict {e}")


query.get_result_stream(stopper).pipe(ops.take(100)).subscribe(
    on_next=lambda i: handle_result(i),
    on_error=lambda e: print(f"error {e}"),
    on_completed=lambda: stopper.stop(),
)

query.delete()
