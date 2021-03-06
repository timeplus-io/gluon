import streamlit as st

import os

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
st.write(
    "This is a case where we use linear regression to predict one of the car's gas usage"
)
st.write(
    "The query we used is `select time, gas_percent, speed_kmh from car_live_data where cid='c00004'`"
)
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
st.write(env.info())

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


def handle_result(result):
    model = st.session_state["model"]
    metric = st.session_state["metric"]

    data = result
    time = data[0].timestamp()
    speed = data[2]
    value = data[1]
    x = {"time": time, "speed": speed}
    y = float(value)
    try:
        # st.write(f"predict one x={x},y ={y}")
        y_pred = model.predict_one(x)
        # st.write(f"predict one result {y_pred}")
        metric = metric.update(y, y_pred)
        # st.write(f"metric is {metric}")
        model = model.learn_one(x, y)

        col = ["time", "value", "value_type"]
        row_original = [time, y, "gas"]
        row_predict = [time, y_pred, "predict_gas"]
        row_metrics = [time, metric.get(), "mae"]
        row_speed = [time, speed, "speed"]
        df = pd.DataFrame(
            [row_original, row_predict, row_metrics, row_speed], columns=col
        )

        if "chart" not in st.session_state:
            c = (
                alt.Chart(df)
                .mark_line()
                .encode(
                    x="time",
                    y="value",
                    color="value_type",
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
