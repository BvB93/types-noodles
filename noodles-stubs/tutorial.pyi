from collections.abc import Iterable, Sequence
from typing import Any, TypeVar

from graphviz import Digraph
from noodles import schedule, schedule_hint
from noodles.interface import PromisedObject
from noodles.workflow import Workflow

_NT = TypeVar("_NT", bound=complex)
_T = TypeVar("_T")

@schedule
def echo_add(x: _NT, yx: _NT) -> _NT: ...
@schedule
def add(x: _NT, yx: _NT) -> _NT: ...
@schedule_hint()
def log_add(x: _NT, yx: _NT) -> _NT: ...
@schedule
def sub(x: _NT, yx: _NT) -> _NT: ...
@schedule
def mul(x: _NT, yx: _NT) -> _NT: ...
@schedule
def accumulate(lst: Iterable[_NT], start: _NT = ...) -> _NT: ...
def get_workflow_graph(promise: PromisedObject[Any] | Workflow[Any]) -> Digraph: ...
def display_workflows(prefix: str, **kwargs: PromisedObject[Any] | Workflow[Any]) -> None: ...
def snip_line(line: Sequence[str], max_width: int, split_at: int) -> str: ...
def display_text(text: str, highlight: Sequence[int] | None = ..., max_width: int = ..., split_at: int | None = ...) -> None: ...
def run_and_print_log(workflow: Workflow[_T], highlight: Sequence[int] | None = ...) -> _T: ...
