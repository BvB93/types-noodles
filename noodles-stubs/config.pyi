import configparser
from typing import TypedDict

class _Config(TypedDict):
    call_by_value: bool

config: _Config

def read_config(filename: str) -> configparser.ConfigParser: ...
