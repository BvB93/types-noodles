from _typeshed import Incomplete
from typing import NamedTuple

from ...lib import Connection
from .xenon import Machine

def xenon_interactive_worker(
    machine, worker_config, input_queue: Incomplete | None = ..., stderr_sink: Incomplete | None = ...
): ...

class XenonInteractiveWorker(Connection):
    worker_config: Incomplete
    job: Incomplete
    machine: Incomplete
    online: bool
    def __init__(self, machine, worker_config) -> None: ...
    def wait_until_running(self, callback: Incomplete | None = ...) -> None: ...
    def close(self) -> None: ...

class RemoteWorker(NamedTuple):
    name: Incomplete
    lock: Incomplete
    max: Incomplete
    jobs: Incomplete
    source: Incomplete
    sink: Incomplete

class DynamicPool(Connection):
    workers: Incomplete
    machine: Incomplete
    job_queue: Incomplete
    result_queue: Incomplete
    wlock: Incomplete
    plock: Incomplete
    count: Incomplete
    def __init__(self, machine: Machine) -> None: ...
    def close_all(self) -> None: ...
    def add_xenon_worker(self, worker_config) -> None: ...
