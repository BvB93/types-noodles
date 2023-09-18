import hashlib
from collections.abc import Mapping
from typing import Any, TypeVar

_HT = TypeVar("_HT", bound=hashlib._Hash)

def update_object_hash(m: _HT, obj: Any) -> _HT: ...
def prov_key(job_msg: Mapping[str, Any], extra: Any | None = ...): ...
