# Getting Started with Agile Agents Platform

Welcome to the Agile Agents platform! This guide will help you get started with setting up and using the platform to leverage decentralized GPU compute resources for your AI and machine learning projects.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- Python 3.8 or higher
- Docker
- Git

## Installation

1. **Clone the Repository**

   Start by cloning the Agile Agents repository to your local machine:

   ```bash
   git clone https://github.com/ruvnet/agileagents.git
   cd agileagents
   ```

2. **Set Up Virtual Environment**

   Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the central server application:

```bash
uvicorn central-server.app.main:app --reload
```

To run a worker node application:

```bash
python worker-node/app/main.py
```

## Submitting Jobs

Use the client library to submit jobs to the central server. Ensure you have installed the client library in your project:

```bash
pip install ./client-library
```

Example of submitting a job:

```python
from distexgpu.client import Client

client = Client(api_key="your_api_key")
job = client.submit_job(gpu_requirements=2, input_data={"data": "example"})
print(job.status())
```

## Monitoring and Management

The platform provides a web-based UI for monitoring and managing jobs and worker nodes. Access the UI by navigating to:

```
http://localhost:8000
```

## Next Steps

Explore the documentation to learn more about advanced features, including job scheduling, result retrieval, and worker node management.

Thank you for choosing Agile Agents platform. Happy computing!
