import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(1, root_dir)

# from src.num import NUM
# from src.sym import SYM
from src.l import l
from src.row import ROW
import src.tricks as tricks

# def test_Num():
#     num = NUM()
#     nums = [5, 5, 5, 5, 10, 10]
#     for n in nums:
#         num.add(n)
#     return 40//6 == num.mid() and 2.581988897471611 == num.div()

# def test_Sym():
#     sym = SYM()
#     syms = ['s', 's', 'd', 'd', 's', 's']
#     for s in syms:
#         sym.add(s)
#     return 's' == sym.mid and 0.9182958340544896 == sym.div()

import os
import subprocess
import sys
import ast
import unittest

class TestGateScript(unittest.TestCase):
    def test_stats_task(self):
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "gate.py"))
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "auto93.csv"))
        task = "stats"

        # Construct the command with sys.argv inputs
        command = [sys.executable, script_path, "-f", file_path, "-t", task]

        try:
            # Run the command and capture the output
            output = subprocess.check_output(command, universal_newlines=True, cwd=os.path.dirname(__file__))
            
            # Parse the output and compare with expected result
            expected_output = '{".N": 398, "Acc+": 15.57, "Lbs-": 2970.42, "Mpg+": 23.84}'
            formatted_expected = ast.literal_eval(expected_output)
            formatted_output = ast.literal_eval(output)
            
            self.assertEqual(formatted_output, formatted_expected, f"Test failed. Expected: {formatted_expected}, Actual: {formatted_output}")
            
            print("Test passed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error while running the command: {e}")
            print(f"Command: {' '.join(command)}")
            self.fail("Test failed.")
    
    def test_rnd_test(self):
       self.assertEqual(l().rnd(23.324234), 23.32)
       self.assertEqual(l().rnd(23.324234, 3), 23.324)
       
    def test_tricks_coerce(self):
        self.assertEqual(tricks.coerce("5"), 5)
        self.assertEqual(tricks.coerce(5), 5)
    
    def test_row_object(self):
        row_data = ["Mpg", 5, "Po", "Area"]
        self.assertEqual(ROW(row_data).cells, row_data)
    
        
    
        

if __name__ == "__main__":
    unittest.main()
