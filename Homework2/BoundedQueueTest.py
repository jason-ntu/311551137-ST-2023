from unittest import TestCase
from BoundedQueue import BoundedQueue

# The five methods tested are: BoundedQueue(), enqueue(), dequeue(), is_empty(), is_full()
# The following characteristics have been identified and are used to generate tests for the methods:
# C1: capacity >= 0
# C2: input non null object
# C3: queue is empty
# C4: queue is full
# Each characteristic has a boolean partition.
class BoundedQueueTest(TestCase):

    def setUp(self):
        self.bq = BoundedQueue(2)
        self.bq.enqueue("obj1")

    # 2 Tests for BoundedQueue method BoundedQueue()
    # The 1 characteristics associated with BoundedQueue() is: C1
    # Test 1 of BoundedQueue(): test_BoundedQueue_BaseCase(): C1-T
    def test_BoundedQueue_BaseCase(self):
        self.assertGreaterEqual(self.bq.capacity, 0)

    # Test 2 of BoundedQueue(): test_BoundedQueue_C1(): C1-F
    def test_BoundedQueue_C1(self):
        with self.assertRaisesRegex(ValueError, 'BoundedQueue.constructor'):
            BoundedQueue(-1)

    # 3 Tests for BoundedQueue method enqueue()
    # The 2 characteristics associated with enqueue() is: C2, C4
    # Test 1 of enqueue(): test_enqueue_BaseCase(): C2-T, C4-F
    def test_enqueue_BaseCase(self):
        self.bq.enqueue("obj2")
        self.assertIn("obj2", self.bq.elements)

    # Test 2 of enqueue(): test_enqueue_C2(): C2-F, C4-F
    def test_enqueue_C2(self):
        with self.assertRaisesRegex(TypeError, 'BoundedQueue.enqueue'):
            self.bq.enqueue(None)

    # Test 3 of enqueue(): test_enqueue_C4(): C2-T, C4-T
    def test_enqueue_C4(self):
        self.bq.enqueue("obj2")
        with self.assertRaisesRegex(RuntimeError, 'BoundedQueue.enqueue'):
            self.bq.enqueue("obj3")

    # 2 Tests for BoundedQueue method dequeue()
    # The 2 characteristics associated with dequeue() is: C2, C3
    # Test 1 of dequeue(): test_dequeue_BaseCase(): C2-T, C3-F
    def test_dequeue_BaseCase(self):
        self.bq.dequeue()
        self.assertNotIn("obj1", self.bq.elements)

    # Test 2 of dequeue(): test_dequeue_C3(): C2-T, C3-T
    def test_dequeue_C3(self):
        self.bq.dequeue()
        with self.assertRaisesRegex(RuntimeError, 'BoundedQueue.dequeue'):
            self.bq.dequeue()

    # 2 Tests for BoundedQueue method is_empty()
    # The 2 characteristics associated with is_empty() is: C3
    # Test 1 of is_empty(): test_is_empty_BaseCase(): C3-F
    def test_is_empty_BaseCase(self):
        self.assertFalse(self.bq.is_empty())

    # Test 2 of is_empty(): test_is_empty_BaseCase(): C3-T
    def test_is_empty_C3(self):
        self.bq.dequeue()
        self.assertTrue(self.bq.is_empty())

    # 2 Tests for BoundedQueue method is_full()
    # The 2 characteristics associated with is_full() is: C4
    # Test 1 of is_full(): test_is_full_BaseCase(): C4-F
    def test_is_full_BaseCase(self):
        self.assertFalse(self.bq.is_full())

    # Test 2 of is_full(): test_is_full_BaseCase(): C4-T
    def test_is_full_C4(self):
        self.bq.enqueue("obj2")
        self.assertTrue(self.bq.is_full())
