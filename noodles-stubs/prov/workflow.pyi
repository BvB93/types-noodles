from _typeshed import Incomplete
from collections.abc import Generator, Iterable
from typing import Any

from ..serial import Registry
from ..workflow import FunctionNode, Workflow
from ..workflow.arguments import ArgumentAddress

def links(wf: Workflow[Any], i: int, deps: Iterable[int]) -> Generator[tuple[ArgumentAddress, Incomplete | None], None, None]: ...
def empty_args(n: FunctionNode[Any]) -> Generator[ArgumentAddress, None, None]: ...
def set_global_provenance(wf: Workflow[Any], registry: Registry) -> None: ...
