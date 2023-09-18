from _typeshed import Incomplete

class Turtle:
    dx: Incomplete
    dy: Incomplete
    stack: Incomplete
    def __init__(self, x, y, d) -> None: ...
    d: Incomplete
    def turn(self, r) -> None: ...
    def move(self) -> None: ...
    def push(self) -> None: ...
    def pop(self) -> None: ...
    x: Incomplete
    y: Incomplete
    def jump(self, x, y, d) -> None: ...

class Canvas:
    width: Incomplete
    height: Incomplete
    turtle: Incomplete
    field: Incomplete
    def __init__(self, width, height, turtle: Incomplete | None = ...) -> None: ...
    def put(self, s): ...
    def render(self): ...

class LSystem:
    axiom: Incomplete
    rules: Incomplete
    def __init__(self, axiom, rules) -> None: ...
    def compute(self, n): ...

def make_frame(w, h): ...