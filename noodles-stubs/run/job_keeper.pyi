import threading
import types
from _typeshed import Incomplete
from collections.abc import Generator
from typing import IO, TypeVar
from typing_extensions import Self

from ..lib import EndOfQueue, coroutine
from ..serial import Registry
from .messages import EndOfWork, JobMessage
from .scheduler import Job

_T = TypeVar("_T")

class JobKeeper(dict[str, Job[_T]]):
    keep: bool
    lock: threading.Lock
    workflows: dict[int, Incomplete]
    def __init__(self, keep: bool = ...) -> None: ...
    def register(self, job: Job[_T]) -> JobMessage[_T]: ...
    def __delitem__(self, key: str) -> None: ...
    def store_result(self, key: str, status: str, value: _T, err: None | Exception) -> None: ...
    @coroutine
    def message(self) -> Generator[None, None | EndOfQueue | tuple[str, str, _T, None | Exception], None]: ...

class JobTimer(dict[str, Job[_T]]):
    workflows: dict[int, Incomplete]
    fo: IO[str]
    owner: bool
    def __init__(self, timing_file: str | IO[str], registry: Registry | None = ...) -> None: ...
    def register(self, job: Job[_T]) -> JobMessage[_T]: ...
    def __delitem__(self, key: str) -> None: ...
    @coroutine
    def message(self) -> Generator[None, None | EndOfWork | tuple[str, str, _T, None | Exception], None]: ...
    def start(self, key: str, value: _T, err: None | Exception) -> None: ...
    def done(self, key: str, value: _T, err: None | Exception) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, e_type: type[BaseException], e_value: BaseException, e_tb: types.TracebackType) -> None: ...
