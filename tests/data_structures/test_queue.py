import unittest
from my_package.data_structures.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_initialization(self):
        self.queue = Queue([2, 5, 7, 6, 3, 5, 67])
        self.assertEqual(len(self.queue), 7)

    def test_enqueue(self):
        self.queue = Queue([2, 5, 7, 6, 3, 5, 67])
        self.queue.enqueue(45)
        self.assertEqual(len(self.queue), 8)
        self.assertEqual(self.queue.peek, 45)

    def test_dequeue(self):
        self.queue = Queue([2, 5, 7, 6, 3, 5, 67])
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 6)


if __name__ == "__main__":
    unittest.main()
