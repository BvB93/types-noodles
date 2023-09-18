from _typeshed import Incomplete
from collections.abc import Generator, Iterator
from typing import Any, Generic, TypeVar

from ..interface.decorator import _Hints
from ..lib import Connection
from ..workflow import FunctionNode, Workflow
from .job_keeper import JobKeeper
from .messages import JobMessage

_T = TypeVar("_T")

class Job(Generic[_T]):
    workflow: Workflow[_T]
    node_id: int
    db_id: int | None
    log: list[tuple[float, str, None | _T, None | Exception]]
    sched_time: float
    start_time: float
    def __init__(self, workflow: Workflow[_T], node_id: int) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    @property
    def node(self) -> FunctionNode[_T]: ...
    @property
    def name(self) -> str: ...
    @property
    def hints(self) -> _Hints: ...
    @property
    def is_root_node(self) -> bool: ...

class DynamicLink(Generic[_T]):
    source: Workflow[_T]
    target: Workflow[_T]
    node: int
    def __init__(self, source: Workflow[_T], target: Workflow[_T], node: int) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...

error_msg_1: str

class Scheduler(Generic[_T]):
    jobs: JobKeeper[_T]
    dynamic_links: dict[int, DynamicLink[_T]]
    count: int
    key_map: dict[str, Incomplete]
    verbose: bool
    handle_error: Incomplete
    def __init__(
        self, verbose: bool = ..., error_handler: Incomplete | None = ..., job_keeper: JobKeeper[_T] | None = ...
    ) -> None: ...
    def run(self, connection: Connection, master: Workflow[_T]) -> _T: ...
    def schedule(self, job: Job[_T], sink: Generator[object, JobMessage[_T], object]) -> None: ...
    def add_workflow(
        self, wf: Workflow[_T], target: Workflow[_T], node: int, sink: Generator[object, JobMessage[_T], object]
    ) -> None: ...
