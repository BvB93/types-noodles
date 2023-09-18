from collections.abc import Callable
from typing import TypeVar

from ...interface import PromisedObject
from ...lib import Queue, pull
from ...prov.sqlite import JobDB
from ...serial import Registry
from ...workflow import Workflow

_T = TypeVar("_T")

def pass_job(db: JobDB, result_queue: Queue, always_cache: bool = ...) -> pull: ...
def pass_result(db: JobDB, always_cache: bool = ...) -> pull: ...
def run_parallel(
    workflow: Workflow[_T] | PromisedObject[_T],
    *,
    n_threads: int,
    registry: Callable[[], Registry],
    db_file: str,
    echo_log: bool = ...,
    always_cache: bool = ...,
) -> _T: ...
