import time

from river import datasets
from timeplus import Env
from timeplus import Stream, StreamColumn


def local_environment():
    env = Env()
    Env.setCurrent(env)
    return env


def create_stream(name, dataset):
    s = None
    for x, y in dataset:
        if s is None:
            s = Stream().name(name)
            for key in x.keys():
                s.column(StreamColumn().name(key).type("float64"))
            s.column(StreamColumn().name("isAnomaly").type("bool"))

            try:
                s.delete()
            except Exception as e:
                print(f"failed to delete stream {e}")

            time.sleep(3)

            try:
                s.create()
                time.sleep(3)
            except Exception as e:
                print(f"failed to create stream {e}")

        # check the order of keys?
        data = [x[key] for key in x.keys()]
        data.append(y == 1)
        s.insert([data])


env = local_environment()

create_stream("CreditCard", datasets.CreditCard())
