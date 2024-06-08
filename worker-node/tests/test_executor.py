import unittest
from worker_node.app.executor import JobExecutor

class TestJobExecutor(unittest.TestCase):
    def setUp(self):
        self.executor = JobExecutor()

    def test_execute_job(self):
        job_id = "test_job"
        job_data = {"input": "test data"}
        result = self.executor.execute_job(job_id, job_data)
        self.assertIsNotNone(result)
        self.assertEqual(result, "Job execution result", "The job execution result did not match the expected output.")

if __name__ == '__main__':
    unittest.main()
