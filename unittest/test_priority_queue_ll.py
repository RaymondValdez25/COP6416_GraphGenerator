import unittest
import sys
sys.path.append(".")
from pq.priority_queue_ll import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_is_empty(self):
        self.assertTrue(self.ll.is_empty())
        self.ll.insert(("key1", "key2"), 13)
        self.assertFalse(self.ll.is_empty())
    
    def test_insert_and_delete(self):
        self.ll.insert(('key1', 'key2'), 13)
        self.ll.insert(('key3', 'key4'), 54)
        self.ll.insert(('key5', 'key6'), 6)

        self.assertEqual(self.ll.root.key_value_pair,('key5', 'key6'))
        self.assertEqual(self.ll.root.priority,6)

        self.assertEqual(self.ll.root.next.key_value_pair, (('key1', 'key2')))
        self.assertEqual(self.ll.root.next.priority, ((13)))

        self.assertEqual(self.ll.root.next.next.next, None)
        
        # deleting all the elements
        while not self.ll.is_empty():
            self.ll.delete_min()
        
        self.assertTrue(self.ll.is_empty())

if __name__ == "__main__":
    unittest.main()