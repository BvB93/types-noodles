from _typeshed import Incomplete
from collections.abc import Callable
from typing import TypeVar

from .queue import Queue, _QueueState
from .streams import pull

_FT = TypeVar("_FT", bound=Callable[..., object])

def thread_counter(finalize: Callable[[], object]) -> Callable[[_FT], _FT]: ...
def thread_pool(*workers: pull | Incomplete, results: Queue | None = ..., end_of_queue: _QueueState = ...) -> pull: ...
