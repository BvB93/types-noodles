from _typeshed import Incomplete

class Display:
    jobs: Incomplete
    out: Incomplete
    errors: Incomplete
    error_filter: Incomplete
    messages: Incomplete
    def __init__(self, error_filter) -> None: ...
    def start(self, key, job, _) -> None: ...
    def done(self, key, data, msg) -> None: ...
    def error(self, key, _, data) -> None: ...
    def add_job(self, key, job, msg) -> None: ...
    def error_handler(self, job, xcptn) -> None: ...
    def message_handler(self, job, warning) -> None: ...
    def report(self) -> None: ...
    q: Incomplete
    def __call__(self, q) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...
    def wait(self) -> None: ...
