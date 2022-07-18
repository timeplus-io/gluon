import time
import threading

from collections import deque

from timeplus import Stream, StreamColumn, Env


class TimeplusMetricsError(Exception):
    """Exception raised for errors in the timeplus metrics API.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="failed to call timeplus metrics API"):
        self.message = message
        super().__init__(self.message)


class Metrics:
    def __init__(
        self,
        name,
        create_new_metrics=False,
        value_column_names=["value"],
        tag_column_names=[],
    ):
        self._name = name
        self._stream_name = f"_tp_metrics_{self._name}"
        self._create_new_metrics = create_new_metrics
        self._value_column_names = value_column_names
        self._tag_column_names = tag_column_names
        self._logger = Env._current_env._logger
        self._stop = None
        self._lock = threading.Lock()

        self._event_queue = deque([])

        if self._create_new_metrics:
            self._create()
        else:
            self._get()

    def _create(self):
        s = (
            Stream()
            .name(self._stream_name)
            .column(StreamColumn().name("timestamp").type("string"))
            .column(StreamColumn().name("namespace").type("string"))
            .column(StreamColumn().name("subsystem").type("string"))
            .column(StreamColumn().name("tags").type("json"))
        )

        s.event_time_column("to_datetime64(timestamp,9)")

        for name in self._tag_column_names:
            s.column(StreamColumn().name(name).type("string"))

        for name in self._value_column_names:
            s.column(StreamColumn().name(name).type("float64"))

        s.create()
        self._get()

    def _get(self):
        s = Stream().name(self._stream_name)
        s.get()
        self._stream = s
        self._headers = [col["name"] for col in self._stream.data()["columns"]]
        self._ingest_headers = self._headers[:-2]

        self._fix_tag_columns = [
            col["name"]
            for col in self._stream.data()["columns"]
            if col["type"] == "string"
            and col["name"] not in ["timestamp", "namespace", "subsystem"]
        ]

        self._value_coloumns = [
            col["name"]
            for col in self._stream.data()["columns"]
            if col["type"] == "float64"
        ]

    def delete(self):
        if self._stop is not None and not self._stop:
            self.stop()

        s = Stream().name(self._stream_name)
        s.delete()

    def observe(self, namespace, subsystem, values, tags, extra_tages):
        self._logger.debug("header is {}", self._headers)

        data = [str(time.time_ns()), namespace, subsystem]
        data.append(extra_tages)

        if tags is not None:
            if len(tags) != len(self._fix_tag_columns):
                raise TimeplusMetricsError("invalid tag data")
            for t in tags:
                data.append(t)

        if values is not None:
            if len(values) != len(self._value_coloumns):
                raise TimeplusMetricsError("invalid value data")
            for v in values:
                data.append(v)

        self._lock.acquire()
        self._event_queue.append(data)
        self._lock.release()

    def start(self):
        self._job = threading.Thread(target=self._run)
        self._job.start()

    def _run(self):
        self._stop = False
        while True:
            self.flush()
            time.sleep(1)
            if self._stop:
                break

    def flush(self):
        if len(self._event_queue) > 0:
            self._lock.acquire()
            ingestData = list(self._event_queue)
            self._event_queue.clear()
            self._lock.release()

            self._stream.insert(ingestData, headers=self._ingest_headers)

    def stop(self):
        self._stop = True
        self._job.join()
