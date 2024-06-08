import unittest
from worker_node.app.firecracker import FirecrackerManager

class TestFirecrackerManager(unittest.TestCase):
    def setUp(self):
        self.manager = FirecrackerManager()

    def test_create_microvm(self):
        job_id = "test_job"
        microvm_id = self.manager.create_microvm(job_id)
        self.assertTrue(microvm_id.startswith("microvm-"), "MicroVM ID should start with 'microvm-' prefix.")

    def test_start_stop_delete_microvm(self):
        job_id = "test_job"
        microvm_id = self.manager.create_microvm(job_id)
        self.manager.start_microvm(microvm_id)
        # Assuming there's a way to check if a microVM is running, this would be the place to do it.
        self.manager.stop_microvm(microvm_id)
        # Assuming there's a way to check if a microVM is stopped, this would be the place to do it.
        self.manager.delete_microvm(microvm_id)
        # Assuming there's a way to check if a microVM is deleted, this would be the place to do it.

if __name__ == '__main__':
    unittest.main()
