from _typeshed import Incomplete

class WorkerConfig:
    name: Incomplete
    working_dir: Incomplete
    prefix: Incomplete
    exec_command: Incomplete
    n_threads: Incomplete
    registry: Incomplete
    init: Incomplete
    finish: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        *,
        name: Incomplete | None = ...,
        working_dir: Incomplete | None = ...,
        prefix: Incomplete | None = ...,
        exec_command: Incomplete | None = ...,
        n_threads: int = ...,
        registry=...,
        init: Incomplete | None = ...,
        finish: Incomplete | None = ...,
        verbose: bool = ...,
    ) -> None: ...
    def command_line(self): ...
