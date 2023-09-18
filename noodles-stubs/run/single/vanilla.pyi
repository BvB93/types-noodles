from typing import TypeVar

from ...workflow import Workflow

_T = TypeVar("_T")

def run_single(workflow: Workflow[_T]) -> _T: ...
