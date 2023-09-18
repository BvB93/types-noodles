import enum
from collections.abc import Callable, Mapping, Sequence
from typing import Any, NamedTuple, Protocol, TypedDict, TypeVar
from typing_extensions import Self

from ..interface import PromisedObject
from ..workflow import FunctionNode, Workflow
from .registry import Registry, Serialiser, _MakeRec, _RecDict

_T = TypeVar("_T")
_DT = TypeVar("_DT")

class _WorkflowDict(TypedDict):
    root: int
    nodes: list[FunctionNode[Any]]
    links: list[dict[str, Any]]

class _PromisedObjectDict(TypedDict):
    workflow: Workflow[Any]

class _MethodDict(TypedDict):
    cls: str
    method: str

class _BoundethodDict(TypedDict):
    self: Any
    method: str

class _SupportsSerialize(Protocol[_DT]):
    def __serialize__(self, __make_rec: _MakeRec[_DT]) -> _RecDict[_DT]: ...
    def __construct__(self, __data: _DT) -> Self: ...

def ismethod(x: Callable[..., object]) -> bool: ...

class _Serialiser(Serialiser[_T, _DT]):
    def encode(self, obj: _T, make_rec: _MakeRec[_DT]) -> _RecDict[_DT]: ...
    def decode(self, cls: Callable[[_DT], _T], data: _DT) -> _T: ...

class SerAuto(_Serialiser[Serialiser[Any, Any], Any]):
    def __init__(self) -> None: ...

class SerByMembers(_Serialiser[Any, dict[str, Any]]):
    members: list[str]
    def __init__(self, cls: str | Callable[..., object], members: list[str]) -> None: ...

class SerDict(_Serialiser[Mapping[Any, Any], dict[Any, Any]]):
    def __init__(self) -> None: ...

class SerBytes(_Serialiser[bytes, str]):
    def __init__(self) -> None: ...

class SerSequence(_Serialiser[Sequence[Any], list[Any]]):
    def __init__(self, cls: str | Callable[..., object]) -> None: ...

class SerEnum(_Serialiser[enum.Enum, str]):
    def __init__(self, cls: str | Callable[..., object]) -> None: ...

class SerNamedTuple(_Serialiser[NamedTuple, dict[str, Any]]):
    def __init__(self, cls: str | Callable[..., object]) -> None: ...

class SerSlice(_Serialiser[slice, list[int | None]]):
    def __init__(self) -> None: ...

class SerWorkflow(_Serialiser[Workflow[Any], _WorkflowDict]):
    def __init__(self) -> None: ...

class SerPromisedObject(_Serialiser[PromisedObject[Any], _PromisedObjectDict]):
    def __init__(self) -> None: ...

class SerMethod(_Serialiser[Callable[..., Any], _MethodDict]):
    def __init__(self) -> None: ...

class SerBoundMethod(_Serialiser[Callable[..., Any], _BoundethodDict]):
    def __init__(self) -> None: ...

class SerImportable(_Serialiser[Any, str]):
    def __init__(self) -> None: ...

class SerNode(_Serialiser[FunctionNode[Any], dict[str, Any]]):
    def __init__(self) -> None: ...

class SerUnwrapped(_Serialiser[Callable[..., Any], str]):
    def __init__(self) -> None: ...

def registry() -> Registry: ...
