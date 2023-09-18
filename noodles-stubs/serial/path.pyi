import pathlib

from .base import _Serialiser

class SerPath(_Serialiser[pathlib.Path, str]):
    def __init__(self) -> None: ...
