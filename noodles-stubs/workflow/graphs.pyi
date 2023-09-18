from collections.abc import Iterable, Mapping
from typing import TypeVar

_KT = TypeVar("_KT")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")

def find_links_to(links: Mapping[_KT, Iterable[tuple[_T1, _T2]]], node: _T1) -> dict[_T2, _KT]: ...
def invert_links(links: Mapping[_KT, Iterable[tuple[_T1, _T2]]]) -> dict[_KT, dict[_T2, _KT]]: ...
