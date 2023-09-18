from typing import TypeVar

from ...workflow.model import Workflow

_T = TypeVar("_T")

def run_parallel(workflow: Workflow[_T], n_threads: int) -> _T: ...
