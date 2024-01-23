from src.l import l
import unittest

class TestLScript(unittest.TestCase):
    def test_rnd_test(self):
       self.assertEqual(l().rnd(23.324234), 23.32)
       self.assertEqual(l().rnd(23.324234, 3), 23.324)

if __name__ == "__main__":
    unittest.main()