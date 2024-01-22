import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(1, root_dir)

import unittest
from unittest.mock import MagicMock
from src.num import NUM

class TestLearnFunction(unittest.TestCase):

    #Num test cases start here
    def test_Num(self):
        num = NUM()
        nums = [5, 5, 5, 5, 10, 10]
        for n in nums:
            num.add(n)
        
        self.assertEqual(40 // 6, num.mid())
        self.assertAlmostEqual(2.581988897471611, num.div(), places=12)

        # Test case for the like method in NUM
        x = 9  
        result = num.like(x)
        mu, sd = num.mid(), num.div() + 1E-30
        expected_result = 2.718 ** (-.5 * (x - mu) ** 2 / (sd ** 2)) / (sd * 2.5 + 1E-30)

        self.assertEqual(expected_result, result)


    
    


    #Num test cases end here