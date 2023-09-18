from .as_dict import AsDict as AsDict
from .base import registry as _base
from .namedtuple import registry as _namedtuple
from .numpy import registry as _numpy
from .path import SerPath as SerPath
from .pickle import registry as _pickle
from .reasonable import Reasonable as Reasonable
from .registry import RefObject as RefObject, Registry as Registry, Serialiser as Serialiser

base = _base
namedtuple = _namedtuple
numpy = _numpy
pickle = _pickle
