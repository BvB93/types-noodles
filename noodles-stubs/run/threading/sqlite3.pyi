from collections.abc import Callable
from typing import Any, TypeVar

from ...interface import PromisedObject
from ...lib import Queue, pull
from ...prov.sqlite import JobDB
from ...serial import Registry
from ...workflow import Workflow

_T = TypeVar("_T")

def pass_job(db: JobDB[Any], result_queue: Queue, always_cache: bool = ...) -> pull: ...
def pass_result(db: JobDB[Any], always_cache: bool = ...) -> pull: ...
def run_parallel(
    workflow: Workflow[_T] | PromisedObject[_T],
    *,
    n_threads: int,
    registry: Callable[[], Registry],
    db_file: str,
    echo_log: bool = ...,
    always_cache: bool = ...,
) -> _T: ...
