import os
import time

from rx import operators as ops
from timeplus import Stream, StreamColumn, Query, Env, Type


# initialize timeplus environment
api_key = "jGphdqC2PjCayDzjyck76LbNpXVSThL1vTkOVVbuoga5E0LrbO-JCK9FEJrL"
host = "duckbill.beta.timeplus.com"
env = Env().schema("https").host(host).port("444").api_key(api_key)
Env.setCurrent(env)


# curl -X GET   'localhost:9444/proton/metastore/neutron?key_prefix=query' | jq '.data | keys[]'  > query_keys.txt
query_id_file = open("./query_keys.txt", "r")
lines = query_id_file.readlines()

for line in lines:
    id = line[7:-2]
    q = Query().id(id)
    try:
        q.delete()
    except:
        pass
