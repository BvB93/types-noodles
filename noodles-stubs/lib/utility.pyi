from collections.abc import Callable, Mapping
from typing import Any, TypeVar, overload

_KT = TypeVar("_KT")
_T = TypeVar("_T")
_RT = TypeVar("_RT")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_FT = TypeVar("_FT", bound=Callable[..., object])

def object_name(obj: Callable[..., object]) -> str: ...
def look_up(name: str) -> Any: ...
def importable(obj: object) -> bool: ...
def unzip_dict(d: Mapping[_KT, tuple[_T1, _T2]]) -> tuple[dict[_KT, _T1], dict[_KT, _T2]]: ...
def unwrap(f: _FT) -> _FT: ...
def is_unwrapped(f: Callable[..., object]) -> bool: ...
@overload
def deep_map(f: Callable[[_T], dict[_KT, Any]], root: _T) -> dict[_KT, Any]: ...
@overload
def deep_map(f: Callable[[_T], list[Any] | tuple[Any, ...]], root: _T) -> list[Any]: ...
@overload
def deep_map(f: Callable[[_T], _RT], root: _T) -> _RT: ...
def inverse_deep_map(f: Callable[[Any], _RT], root: Any) -> _RT: ...