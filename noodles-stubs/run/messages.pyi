import enum
from typing import Any, Generic, Iterator, Literal, TypeVar

from noodles.interface.decorator import _Hints
from noodles.serial import Reasonable
from noodles.workflow import FunctionNode

_T = TypeVar("_T")

class _WorkEnum(enum.Enum):
    EndOfWork: type[object]

EndOfWork = Literal[_WorkEnum.EndOfWork]

class JobMessage(Reasonable, Generic[_T]):
    key: int
    node: FunctionNode[_T]
    def __init__(self, key: int, node: FunctionNode[_T]) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    @property
    def hints(self) -> _Hints: ...

class ResultMessage(Reasonable):
    key: int
    status: str
    value: None | Any
    msg: None | Exception
    def __init__(self, key: int, status: str, value: None | Any, msg: None | Exception) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...

class PilotMessage(Reasonable):
    msg: None | Exception
    def __init__(self, msg: None | Exception, **kwargs: Any) -> None: ...
    def __getattr__(self, key: str) -> Any: ...
