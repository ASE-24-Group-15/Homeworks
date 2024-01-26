import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(1, root_dir)

from src.l import l
import unittest

class TestLScript(unittest.TestCase):
    def test_rnd_test(self):
       self.assertEqual(l().rnd(23.324234), 23.32)
       self.assertEqual(l().rnd(23.324234, 3), 23.324)

if __name__ == "__main__":
    unittest.main()