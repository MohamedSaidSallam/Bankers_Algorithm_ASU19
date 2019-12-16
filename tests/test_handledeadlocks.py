import unittest
from Bankers_Algorithm_ASU19.main import handleDeadlock

class testHandleDeadlocks(unittest.TestCase):
    def test_normalCase1(self):
        reply = handleDeadlock(
            5,
            3,
            [0, 0, 0],
            [[0, 1, 0], [4, 0, 2], [3, 0, 3], [3, 1, 1], [0, 0, 4]],
            [[500, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]],
        )
        self.assertEqual(reply, [0])

    def test_normalCase2(self):
        reply = handleDeadlock(
            5,
            3,
            [0, 0, 0],
            [[0, 1, 0], [4, 0, 2], [3, 0, 3], [3, 1, 1], [0, 0, 4]],
            [[500, 1, 0], [400, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]],
        )
        self.assertEqual(set(reply), set([0, 1]))

    def test_normalCase3(self):
        reply = handleDeadlock(
            5,
            3,
            [3, 3, 2],
            [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]],
            [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]],
        )
        self.assertEqual(reply, [])

