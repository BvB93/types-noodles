import enum
import inspect
from collections.abc import Callable, Generator, Iterable
from typing import Any, Literal, NamedTuple

Empty = inspect._empty

class ArgumentKind(enum.Enum):
    regular: Literal[1]
    variadic: Literal[2]
    keyword: Literal[3]

class ArgumentAddress(NamedTuple):
    kind: ArgumentKind
    name: str
    key: None | str | int

class Argument(NamedTuple):
    address: Any
    value: Any

def serialize_arguments(bound_args: inspect.BoundArguments) -> Generator[ArgumentAddress, None, None]: ...
def ref_argument(bound_args: inspect.BoundArguments, address: ArgumentAddress) -> Any: ...
def set_argument(bound_args: inspect.BoundArguments, address: ArgumentAddress, value: Any) -> None: ...
def format_address(address: ArgumentAddress) -> str: ...
def get_arguments(bound_args: inspect.BoundArguments) -> list[tuple[ArgumentAddress, Any]]: ...
def bind_arguments(
    f: Callable[..., object], arguments: Iterable[list[tuple[ArgumentAddress, Any]]]
) -> inspect.BoundArguments: ...
