from _typeshed import Incomplete
from collections.abc import Callable, Generator
from typing import Any, Generic, TypeVar
from typing_extensions import Self

from .coroutine import coroutine as coroutine

_T = TypeVar("_T")

class stream:
    def __rshift__(self, other: Self) -> stream: ...

class pull(stream):
    source: Callable[[], Generator[Any, Any, Any]]
    def __init__(self, fn: Callable[[], Generator[Any, Any, Any]]) -> None: ...
    def __iter__(self) -> Generator[Any, Any, Any]: ...
    def __join__(self, other: pull | Incomplete) -> pull: ...
    def __rshift__(self, other: pull | Incomplete) -> pull: ...
    def __call__(self, *x: Any) -> Generator[Any, Any, Any]: ...

class push(stream):
    sink: Callable[[], Generator[Any, Any, Any]]
    def __init__(self, fn: Callable[[], Generator[Any, Any, Any]], dont_wrap: bool = ...) -> None: ...
    def __lshift__(self, other: push | Incomplete) -> push: ...
    def __rshift__(self, other: push | Incomplete) -> push: ...
    def __join__(self, other: push | Incomplete) -> push: ...
    def __call__(self, *x: Any) -> Generator[Any, Any, Any]: ...

def compose_2(f, g): ...

class pull_map(pull):
    f: Incomplete
    def __init__(self, f) -> None: ...
    def __join__(self, other): ...
    def map(self, source) -> Generator[Incomplete, Incomplete, None]: ...

class push_map(push):
    f: Incomplete
    def __init__(self, f) -> None: ...
    def __join__(self, other): ...
    def map(self, sink) -> Generator[None, Incomplete, None]: ...

def sink_map(f): ...
def branch(*sinks_): ...
def broadcast(*sinks_): ...
def pull_from(iterable): ...
def push_from(iterable): ...
def patch(source, sink) -> None: ...
