from pydantic import BaseModel, Field
from typing import Optional, List

class Job(BaseModel):
    id: str
    worker_id: str
    status: str
    input_data: dict
    result_data: Optional[dict] = None

class Worker(BaseModel):
    id: str
    ip_address: str
    capacity: int
    utilization: int

class JobSubmission(BaseModel):
    worker_id: str
    input_data: dict

class JobStatus(BaseModel):
    job_id: str
    status: str

class WorkerHeartbeat(BaseModel):
    worker_id: str
    utilization: int
