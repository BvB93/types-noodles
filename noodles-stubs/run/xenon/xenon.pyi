from _typeshed import Incomplete

from ..remote.worker_config import WorkerConfig

class XenonJobConfig(WorkerConfig):
    time_out: Incomplete
    xenon_job_description: Incomplete
    def __init__(
        self,
        *,
        queue_name: Incomplete | None = ...,
        environment: Incomplete | None = ...,
        time_out: int = ...,
        scheduler_arguments: Incomplete | None = ...,
        **kwargs,
    ) -> None: ...

class Machine:
    name: Incomplete
    scheduler_adaptor: Incomplete
    location: Incomplete
    credential: Incomplete
    jobs_properties: Incomplete
    files_properties: Incomplete
    def __init__(
        self,
        *,
        name: Incomplete | None = ...,
        scheduler_adaptor: str = ...,
        location: Incomplete | None = ...,
        credential: Incomplete | None = ...,
        jobs_properties: Incomplete | None = ...,
        files_properties: Incomplete | None = ...,
    ) -> None: ...
    @property
    def scheduler_args(self): ...
    @property
    def scheduler(self): ...
    @property
    def file_system(self): ...
