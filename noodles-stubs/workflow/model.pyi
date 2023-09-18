import inspect
from _typeshed import Incomplete
from collections.abc import Callable, Iterator
from typing import Any, Generic, NamedTuple, Protocol, TypeVar
from typing_extensions import TypeGuard

from ..interface.decorator import _Hints
from .arguments import ArgumentAddress

class _SupportsWorkflow(Protocol[_T]):
    @property
    def _workflow(self) -> Workflow[_T]: ...

_T = TypeVar("_T")

class NodeData(NamedTuple, Generic[_T]):
    function: Callable[..., _T]
    arguments: list[tuple[ArgumentAddress, Any]]
    hints: Incomplete

class FunctionNode(Generic[_T]):
    @staticmethod
    def from_node_data(data: NodeData[_T]) -> FunctionNode[_T]: ...
    foo: Callable[..., _T]
    bound_args: inspect.BoundArguments
    hints: _Hints
    result: _T | type[inspect._empty]
    prov: None
    def __init__(
        self, foo: Callable[..., _T], bound_args: inspect.BoundArguments, hints: _Hints, result: _T | type[inspect._empty] = ...
    ) -> None: ...
    def apply(self) -> _T: ...
    @property
    def data(self) -> NodeData: ...

class Workflow(Generic[_T]):
    root: int
    nodes: dict[int, FunctionNode[_T]]
    links: dict[int, set[tuple[int, ArgumentAddress]]]
    def __init__(
        self, root: int, nodes: dict[int, FunctionNode[_T]], links: dict[int, set[tuple[int, ArgumentAddress]]]
    ) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    @property
    def root_node(self) -> FunctionNode[_T]: ...
    @property
    def prov(self) -> None: ...
    @property
    def inverse_links(self) -> dict[int, set[int]]: ...
    def create_inverse_links(self) -> None: ...

def is_workflow(x: object) -> TypeGuard[Workflow[Any] | _SupportsWorkflow[Any]]: ...
def get_workflow(x: Workflow[_T] | _SupportsWorkflow[_T]) -> Workflow[_T]: ...
def is_node_ready(node: FunctionNode[Any]) -> bool: ...
