from typing import Any, TypedDict

import filelock
import numpy as np
import numpy.typing as npt

from .base import _Serialiser
from .registry import Registry

class _HDF5Dict(TypedDict):
    filename: str
    path: str

class SerNumpyArray(_Serialiser[npt.NDArray[Any], str]):
    def __init__(self) -> None: ...

class SerNumpyScalar(_Serialiser[np.generic, str]):
    def __init__(self) -> None: ...

class SerNumpyArrayToFile(_Serialiser[str, str]):
    file_prefix: str
    def __init__(self, file_prefix: str | None = ...) -> None: ...

def array_sha256(a: npt.NDArray[Any]) -> str: ...

class SerNumpyArrayToHDF5(_Serialiser[npt.NDArray[Any], _HDF5Dict]):
    filename: str
    lock: filelock.FileLock
    def __init__(self, filename: str, lockfile: filelock.FileLock) -> None: ...

class SerUFunc(_Serialiser[np.ufunc, str]):
    def __init__(self) -> None: ...

def arrays_to_file(file_prefix: str | None = ...) -> Registry: ...
def arrays_to_string(file_prefix: str | None = ...) -> Registry: ...
def arrays_to_hdf5(filename: str = ...) -> Registry: ...

registry = arrays_to_string
