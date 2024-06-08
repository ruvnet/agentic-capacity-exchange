import pytest

from distexgpu.client import Client
from distexgpu.exceptions import CentralServerError, WorkerNodeError, ClientLibraryError

def test_submit_job():
    client = Client(api_key="test_api_key")
    response = client.submit_job(gpu_requirements=2, input_data={"data": "test"})
    assert response["status"] == "submitted", "Job submission failed"

def test_check_job_status():
    client = Client(api_key="test_api_key")
    response = client.check_job_status(job_id="12345")
    assert response["status"] == "completed", "Job status check failed"

def test_retrieve_results():
    client = Client(api_key="test_api_key")
    response = client.retrieve_results(job_id="12345")
    assert "results" in response, "Failed to retrieve job results"

def test_submit_job_error_handling():
    client = Client(api_key="test_api_key")
    with pytest.raises(CentralServerError):
        client.submit_job(gpu_requirements=2, input_data={"data": "test"})

def test_check_job_status_error_handling():
    client = Client(api_key="test_api_key")
    with pytest.raises(WorkerNodeError):
        client.check_job_status(job_id="12345")

def test_retrieve_results_error_handling():
    client = Client(api_key="test_api_key")
    with pytest.raises(ClientLibraryError):
        client.retrieve_results(job_id="12345")
