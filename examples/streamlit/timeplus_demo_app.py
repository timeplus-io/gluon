import streamlit as st

import time

import pandas as pd
import numpy as np

from timeplus import Stream, Query

from timeplus import Stopper
from rx import operators as ops

st.title("Timeplus Platform")
st.write("Fast + powerful real-time analytics made intuitive.")
st.write("See https://timeplus.com")

s = Stream().name("car_live_data").get()
query = Query().sql("select * from clicks").create()

time.sleep(5)
st.write(query.stat())
st.write(query.status())
st.write(query.header())

stopper = Stopper()
query.get_result_stream(stopper).pipe(ops.take(3)).subscribe(
    on_next=lambda i: st.write(f"get one result {i}"),
    on_error=lambda e: print(f"error {e}"),
    on_completed=lambda: stopper.stop(),
)
