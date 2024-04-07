import unittest
import sys
sys.path.append(".")
from pq.priority_queue_bmh import BinaryMinHeap


class TestBinaryMinHeap(unittest.TestCase):

    def setUp(self):
        self.min_heap = BinaryMinHeap()

    def test_is_empty(self):
        self.assertTrue(self.min_heap.is_empty())
        self.min_heap.insert(("key1", "key2"), 13)
        self.assertFalse(self.min_heap.is_empty())
    
    def test_insert_and_delete(self):
        self.min_heap.insert(('key1', 'key2'), 13)
        self.min_heap.insert(('key3', 'key4'), 54)
        self.min_heap.insert(('key5', 'key6'), 6)
        min_size_after_insertion = 3
        self.assertEqual(self.min_heap.Heap,[0, (('key5', 'key6'), 6),
                                            (('key3', 'key4'), 54),
                                            (('key1', 'key2'), 13)])
        # testing the size attribute
        self.assertEqual(self.min_heap.size, min_size_after_insertion)
        
        # deleting all the elements
        while self.min_heap.size:
            self.min_heap.delete_min()
        
        self.assertTrue(self.min_heap.is_empty())

    def test_swap(self):
        self.min_heap.insert(('key1', 'key2'), 13)
        self.min_heap.insert(('key3', 'key4'), 54)
        self.min_heap.insert(('key5', 'key6'), 6)

        # swap takes an indices aka position
        # remember that insertion start from index one because first element in the heap is zero
        expected_heap = [0, (('key1', 'key2'), 13),
                                            (('key3', 'key4'), 54),
                                            (('key5', 'key6'), 6)]
        self.min_heap.swap(1, 3)
        self.assertEqual(self.min_heap.Heap, expected_heap)


if __name__ == "__main__":
    unittest.main()