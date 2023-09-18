from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any

from .streams import pull, push

class Connection:
    source: pull
    sink: push
    aux: None | Incomplete
    online: bool
    def __init__(self, source: pull, sink: push, aux: Incomplete | None = ...) -> None: ...
    def setup(self) -> tuple[Generator[Any, Any, Any], Generator[Any, Any, Any]]: ...
    def __rshift__(self, other: pull) -> Connection: ...
    def __join__(self, other: pull) -> Connection: ...
