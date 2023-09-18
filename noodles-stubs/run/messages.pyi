from _typeshed import Incomplete

from ..serial import Reasonable

class EndOfWork: ...

class JobMessage(Reasonable):
    key: Incomplete
    node: Incomplete
    def __init__(self, key, node) -> None: ...
    def __iter__(self): ...
    @property
    def hints(self): ...

class ResultMessage(Reasonable):
    key: Incomplete
    status: Incomplete
    value: Incomplete
    msg: Incomplete
    def __init__(self, key, status, value, msg) -> None: ...
    def __iter__(self): ...

class PilotMessage(Reasonable):
    msg: Incomplete
    def __init__(self, msg, **kwargs) -> None: ...
