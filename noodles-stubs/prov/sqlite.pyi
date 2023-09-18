from _typeshed import Incomplete
from enum import IntEnum
from typing import NamedTuple

schema: str

class JobEntry(NamedTuple):
    id: Incomplete
    session: Incomplete
    name: Incomplete
    status: Incomplete
    prov: Incomplete
    version: Incomplete
    function: Incomplete
    arguments: Incomplete
    result: Incomplete
    link: Incomplete

class SessionEntry(NamedTuple):
    id: Incomplete
    time: Incomplete
    info: Incomplete

class TimestampEntry(NamedTuple):
    job: Incomplete
    time: Incomplete
    what: Incomplete

class Status(IntEnum):
    INACTIVE: int
    WAITING: int
    STORED: int
    WORKFLOW: int
    DUPLICATE: int
    LINKEE: int

class JobDB:
    attached: Incomplete
    connection: Incomplete
    jobs: Incomplete
    links: Incomplete
    registry: Incomplete
    cur: Incomplete
    lock: Incomplete
    workflows: Incomplete
    session: Incomplete
    def __init__(self, path, registry, info: Incomplete | None = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc, exc_type, stacktrace) -> None: ...
    def __len__(self) -> int: ...
    def __delitem__(self, key) -> None: ...
    def __getitem__(self, key): ...
    def register(self, job): ...
    def store_result(self, key, status, value, _) -> None: ...
    def list_jobs(self): ...
    def get_result(self, db_id): ...
    def add_job_to_db(self, key, job): ...
    def job_exists(self, prov): ...
    def store_result_in_db(self, result, always_cache: bool = ...): ...
    def add_time_stamp(self, db_id, name) -> None: ...
