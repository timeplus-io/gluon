import os
import traceback
from pprint import pprint

from timeplus import View, Environment

api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_HOST")
workspace = os.environ.get("TIMEPLUS_WORKSPACE")

# Configure API key and address
env = Environment().address(api_address).workspace(workspace).apikey(api_key)
view_name = "test_view"


def clean():
    try:
        View(env=env).name(view_name).delete()
    except Exception:
        pass


clean()


try:
    # list all views
    view_list = View(env=env).list()
    pprint(f"there are {len(view_list)} views ")

    # create a new view
    view = (
        View(env=env)
        .name(view_name)
        .query("select * from car_live_data where cid = 'c00001'")
        .create()
    )

    view_list = View(env=env).list()
    pprint(f"there are {len(view_list)} views ")
    pprint(f"view is are {view.metadata()} ")

    clean()

    # create a new materialized view
    view = (
        View(env=env)
        .name(view_name)
        .query("select * from car_live_data where cid = 'c00001'")
        .materialized(True)
        .create()
    )

    view_list = View(env=env).list()
    pprint(f"there are {len(view_list)} views ")
    pprint(f"mv is are {view.metadata()} ")

    clean()
    view_list = View(env=env).list()
    pprint(f"there are {len(view_list)} views ")


except Exception as e:
    pprint(e)
    traceback.print_exc()
