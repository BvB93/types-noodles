from typing import Any

from .base import _Serialiser

class AsDict(_Serialiser[Any, dict[str, Any]]): ...
