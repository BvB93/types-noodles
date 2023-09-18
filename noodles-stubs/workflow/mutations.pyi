from typing import Any, TypeVar

from noodles.workflow import ArgumentAddress, FunctionNode, Workflow

_WT = TypeVar("_WT", bound=Workflow[Any])

def reset_workflow(workflow: _WT) -> _WT: ...
def insert_result(bound_args: FunctionNode[Any], address: ArgumentAddress, value: Any) -> None: ...
