import datetime
import pathlib
import sqlite3
import threading
import types
from _typeshed import Incomplete
from collections import defaultdict
from enum import IntEnum
from typing import Any, Generic, Literal, NamedTuple, TypeVar
from typing_extensions import Self

from noodles.run.messages import JobMessage, ResultMessage
from noodles.run.scheduler import Job
from noodles.serial import Registry
from noodles.workflow import FunctionNode

_T = TypeVar("_T")

schema: str

class JobEntry(NamedTuple):
    id: int
    session: int
    name: str
    status: int
    prov: str
    version: str
    function: str
    arguments: str
    result: str
    link: int

class SessionEntry(NamedTuple):
    id: int
    time: datetime.datetime
    info: str

class TimestampEntry(NamedTuple):
    job: int
    time: datetime.datetime
    what: str

class Status(IntEnum):
    INACTIVE: Literal[0]
    WAITING: Literal[1]
    STORED: Literal[2]
    WORKFLOW: Literal[3]
    DUPLICATE: Literal[4]
    LINKEE: Literal[5]

class JobDB(Generic[_T]):
    attached: defaultdict[int, list[int]]
    connection: sqlite3.Connection
    jobs: dict[int, Job[_T]]
    links: defaultdict[int, list[int]]
    registry: Registry
    cur: sqlite3.Cursor
    lock: threading.Lock
    workflows: dict[Incomplete, Incomplete]
    session: int
    def __init__(self, path: str | pathlib.Path, registry: Registry, info: Any | None = ...) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException], exc: BaseException, stacktrace: types.TracebackType) -> None: ...
    def __len__(self) -> int: ...
    def __delitem__(self, key: int) -> None: ...
    def __getitem__(self, key: int) -> Job[_T]: ...
    def register(self, job: Job[_T]) -> JobMessage[_T]: ...
    def store_result(self, key: int, status: str, value: _T, _: object) -> None: ...
    def list_jobs(self) -> dict[int, FunctionNode[_T]]: ...
    def get_result(self, db_id: int) -> _T: ...
    def add_job_to_db(self, key: int, job: Job[_T]) -> tuple[str, None | ResultMessage]: ...
    def job_exists(self, prov: str) -> bool: ...
    def store_result_in_db(self, result: ResultMessage, always_cache: bool = ...) -> tuple[int, ...]: ...
    def add_time_stamp(self, db_id: int, name: str) -> None: ...
