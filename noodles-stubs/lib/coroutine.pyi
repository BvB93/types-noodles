from collections.abc import Callable, Generator
from typing import TypeVar

_FT = TypeVar("_FT", bound=Callable[..., Generator[object, None, object]])

def coroutine(f: _FT) -> _FT: ...
