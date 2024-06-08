import pytest

from distexgpu.exceptions import CentralServerError, WorkerNodeError, ClientLibraryError

def test_central_server_error():
    with pytest.raises(CentralServerError) as exc_info:
        raise CentralServerError("Central server failed to respond")
    assert "Central server failed to respond" in str(exc_info.value)

def test_worker_node_error():
    with pytest.raises(WorkerNodeError) as exc_info:
        raise WorkerNodeError("Worker node encountered an error")
    assert "Worker node encountered an error" in str(exc_info.value)

def test_client_library_error():
    with pytest.raises(ClientLibraryError) as exc_info:
        raise ClientLibraryError("Client library error occurred")
    assert "Client library error occurred" in str(exc_info.value)
