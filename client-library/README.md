# Client Library for Decentralized GPU Marketplace

This client library provides a high-level interface for interacting with the decentralized GPU marketplace platform. It simplifies the process of submitting jobs, checking job status, and retrieving results from the central server.

## Installation

To install the client library, run:

```bash
pip install distexgpu
```

## Usage

Here is a basic example of how to use the client library:

```python
from distexgpu.client import Client

# Initialize the client with your API key
client = Client(api_key="your_api_key_here")

# Submit a job with GPU requirements and input data
job_id = client.submit_job(gpu_requirements=2, input_data={"data": "test"})

# Check the status of the submitted job
status = client.check_job_status(job_id)

# Retrieve the results of the completed job
results = client.retrieve_results(job_id)

print("Job Status:", status)
print("Job Results:", results)
```

## Features

- **Job Submission**: Easily submit jobs with specific GPU requirements and input data.
- **Job Status Checking**: Check the status of submitted jobs to monitor progress.
- **Result Retrieval**: Retrieve the results of completed jobs.

## Contributing

Contributions to the client library are welcome. Please submit pull requests or open issues to suggest improvements or report bugs.

## License

This client library is licensed under the MIT License.
