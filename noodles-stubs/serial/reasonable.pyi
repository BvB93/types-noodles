from collections.abc import Callable
from typing import Any

from .base import _Serialiser

class Reasonable: ...

class SerReasonableObject(_Serialiser[Any, dict[str, Any]]):
    def __init__(self, cls: str | Callable[..., object]) -> None: ...
