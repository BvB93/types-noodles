from typing import Protocol

class _Args(Protocol):
    registry: str
    name: str
    init: str
    finish: str
    jobdirs: bool
    verbose: bool

def run_online_mode(args: _Args) -> None: ...
