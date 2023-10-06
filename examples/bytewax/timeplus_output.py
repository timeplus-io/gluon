"""Output to Timeplus."""
from bytewax.outputs import DynamicOutput, StatelessSink
from timeplus import Stream, Environment
import logging

__all__ = [
    "TimeplusOutput",
]
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

class _TimeplusSink(StatelessSink):
    def __init__(self, address: str, workspace_id: str, api_key: str, stream: str):
        self.env=Environment().address(address).apikey(api_key).workspace(workspace_id)
        self.stream=Stream(env=self.env).name(stream)
        if self.stream.exist():
            logger.debug("the stream exists")
        else:
            self.stream.column("raw","string").create()
            logger.debug("new stream created")

    def write_batch(self, items):
        rows=[]
        for item in items:
            rows.append([item]) # single column in each row
        self.stream.ingest(["raw"],rows)
        logger.debug(f"inserting data..")

class TimeplusOutput(DynamicOutput):
    def __init__(self, address: str, workspace_id: str, api_key: str, stream: str):
        self.address = address
        self.api_key = api_key
        self.workspace_id = workspace_id
        self.stream=stream
    
    """Write each output item to Proton on that worker.

    Items consumed from the dataflow must look like a string. Use a
    proceeding map step to do custom formatting.

    Workers are the unit of parallelism.

    Can support at-least-once processing. Messages from the resume
    epoch will be duplicated right after resume.

    """

    def build(self, worker_index, worker_count):
        """See ABC docstring."""
        return _TimeplusSink(self.address,self.workspace_id,self.api_key, self.stream)