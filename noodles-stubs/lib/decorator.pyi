from collections.abc import Callable
from typing import Concatenate, ParamSpec, TypeVar

_T = TypeVar("_T")
_P = ParamSpec("_P")
_RT = TypeVar("_RT")

def decorator(f: Callable[Concatenate[_T, _P], _RT]) -> Callable[Concatenate[_T, _P], Callable[[_T], _RT]]: ...
