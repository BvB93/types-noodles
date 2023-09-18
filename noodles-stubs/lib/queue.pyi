import enum
from typing import Any, Literal

from .connection import Connection

class _QueueState(enum.Enum):
    EndOfQueue: type[Any]
    FlushQueue: type[Any]

EndOfQueue = Literal[_QueueState.EndOfQueue]
FlushQueue = Literal[_QueueState.FlushQueue]

class Queue(Connection):
    def __init__(self, end_of_queue: _QueueState = ...) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    def empty(self) -> bool: ...
    def wait(self) -> None: ...
