class CentralServerError(Exception):
    """Exception raised for errors in the central server."""

    def __init__(self, message="Error occurred in the central server"):
        self.message = message
        super().__init__(self.message)


class WorkerNodeError(Exception):
    """Exception raised for errors within the worker node."""

    def __init__(self, message="Error occurred in the worker node"):
        self.message = message
        super().__init__(self.message)


class ClientLibraryError(Exception):
    """Exception raised for errors in the client library."""

    def __init__(self, message="Error occurred in the client library"):
        self.message = message
        super().__init__(self.message)
