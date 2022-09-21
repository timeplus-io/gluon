import time
from timeplus import Query, Env


def handle_result(result):
    Env().logger().info(f"got one result {result}")


def run_query(wait_time):
    Env().logger().info(f"sleep {wait_time} for timeplus restart ")
    time.sleep(wait_time)

    query = Query().name("ad hoc query").sql("select * from iot")
    query.create()

    query.get_result_stream().subscribe(
        on_next=lambda i: handle_result(i),
        on_error=lambda e: run_query(30),
        on_completed=lambda: query.stop(),
    )

    query.delete()


run_query(0)
