from collections.abc import Callable, Sequence
from typing import Any, TypeVar

from noodles import schedule
from noodles.interface import PromisedObject, Quote

_T = TypeVar("_T", bound=PromisedObject[Any])

def find_first(pred: Callable[[_T], bool], lst: Sequence[Quote[_T] | _T]) -> _T | None: ...
@schedule
def s_find_first(pred: Callable[[_T], bool], first: _T, lst: Sequence[Quote[_T] | _T]) -> _T | None: ...
