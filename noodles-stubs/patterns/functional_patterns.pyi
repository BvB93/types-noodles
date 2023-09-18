from collections.abc import Callable, Iterable
from typing import Any, TypeVar

from noodles import schedule
from noodles.interface.decorator import PromisedObject
from noodles.interface.functions import _SupportsGetItem

_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")

@schedule
def all(pred: Callable[[_T], bool], xs: Iterable[_T]) -> bool: ...
@schedule
def any(pred: Callable[[_T], bool], xs: Iterable[_T]) -> bool: ...
@schedule
def filter(pred: Callable[[_T], bool], xs: Iterable[_T]) -> PromisedObject[_T]: ...
@schedule
def fold(fun: Callable[[_T1, _T2], _SupportsGetItem[int, _T3]], state: _T1, xs: Iterable[_T2]) -> PromisedObject[_T3]: ...
@schedule
def map(fun: Callable[[_T1], _T2], xs: Iterable[_T1]) -> PromisedObject[_T2]: ...
@schedule
def zip_with(fun: Callable[[tuple[_T1, _T2]], _T], xs: Iterable[_T1], ys: Iterable[_T2]) -> PromisedObject[_T]: ...
