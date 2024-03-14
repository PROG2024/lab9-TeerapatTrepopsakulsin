"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""


import unittest
from counter import Counter


class TestCounter(unittest.TestCase):

    def test_count_and_increment(self):
        counter = Counter()
        counter.count = 0
        self.assertEqual(0, counter.count)
        self.assertEqual(0, counter.count)
        self.assertEqual(1, counter.increment())
        counter.increment()
        self.assertEqual(2, counter.count)
        self.assertEqual(2, counter.count)

    def test_singleton(self):
        counter1 = Counter()
        counter1.count = 0
        counter1.increment()
        counter1.increment()
        self.assertEqual(2, counter1.count)

        counter2 = Counter()
        self.assertTrue(counter2 is counter1)
        self.assertEqual(2, counter2.count)
        self.assertEqual(3, counter2.increment())
        self.assertEqual(3, counter1.count)
        counter1.increment()
        self.assertEqual(counter1.count, counter2.count)
