from collections.abc import Callable, Iterable, Mapping
from typing import Any, TypeVar

from ..interface.decorator import _Hints
from .model import Workflow

_T = TypeVar("_T")

def from_call(
    foo: Callable[..., _T], args: Iterable[Any], kwargs: Mapping[str, Any], hints: None | _Hints, call_by_value: bool = ...
) -> Workflow[_T]: ...
