import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(1, root_dir)

from src.num import NUM
from src.sym import SYM
from src.cols import COLS
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
    # Data stats test cases start here
    # Define expected outputs for each CSV file
    expected_outputs = {
        "auto93.csv": '{".N": 398, "Acc+": 15.57, "Lbs-": 2970.42, "Mpg+": 23.84}',
        "pom.csv": '{".N": 10000, "Cost-": 369.99, "Completion+": 0.87, "Idle-":0.24}',
        "china.csv": '{".N": 499, "N_effort-": 4277.64}',
        "coc1000.csv": '{".N": 1000, "LOC+": 1013.05, "AEXP-": 2.97, "PLEX-": 3.05, "RISK-": 6.68, "EFFORT-": 30807.5}',
        "coc10000.csv": '{".N": 10000, "Effort-": 30506.37, "Loc+": 1009.04,"Risk-":6.59}',
        "diabetes.csv": '{".N": 768, "class!": "negative"}',
        "soybean.csv": '{".N": 683, "class!": "brown-spot"}',
        "weather.csv": '{".N":14,"play!":"yes"}',
        "nasa93dem.csv": '{".N": 93, "Defects-": 3761.76, "Effort-": 624.41, "Kloc+": 94.02, "Months-": 24.18}',
        "healthCloseIsses12mths0011-easy.csv": '{".N": 10000, "ACC+": -8.53, "MRE-": 92.29, "PRED40+": 17.79}',
        "nasa93demNums.csv": '{".N": 93, "Defects-": 3761.76, "Effort-": 624.41, "Kloc+": 94.02, "Months-": 24.18}',
        "healthCloseIsses12mths0001-hard.csv": '{".N": 10000, "ACC+": 5.15, "MRE-": 82.32, "PRED40+": 22.1}',
    }
    
    def run_test_for_file(self, file_path, expected_output):
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "gate.py"))
        task = "stats"

        # Construct the command with sys.argv inputs
        command = [sys.executable, script_path, "-f", file_path, "-t", task]

        try:
            # Run the command and capture the output
            output = subprocess.check_output(command, universal_newlines=True, cwd=os.path.dirname(__file__))
            
            # Parse the output and compare with expected result
            formatted_expected = ast.literal_eval(expected_output)
            formatted_output = ast.literal_eval(output)

            # Use assertDictEqual to compare dictionaries
            self.assertDictEqual(formatted_output, formatted_expected, f"Test failed for file {file_path}. Expected: {formatted_expected}, Actual: {formatted_output}")
            
            print(f"Test passed for file {file_path}.")
            
        except subprocess.CalledProcessError as e:
            print(f"Error while running the command for file {file_path}: {e}")
            print(f"Command: {' '.join(command)}")
            self.fail(f"Test failed for file {file_path}.")

    def test_multiple_files(self):
        data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
        
        # Get a list of CSV files in the data directory
        csv_files = [file for file in os.listdir(data_dir) if file.endswith(".csv") and not file.startswith("zero")]

        # Run the test for each CSV file
        for csv_file in csv_files:
            file_path = os.path.join(data_dir, csv_file)
            expected_output = self.expected_outputs.get(csv_file, "DefaultExpectedOutput")
            self.run_test_for_file(file_path, expected_output)
    # data stats test cases end here

    def test_rnd_test(self):
       self.assertEqual(l().rnd(23.324234), 23.32)
       self.assertEqual(l().rnd(23.324234, 3), 23.324)
    
    # Row test cases start here
    def test_row_object(self):
        row_data = ["Mpg", 5, "Po", "Area"]
        self.assertEqual(ROW(row_data).cells, row_data)
    # Row test cases end here

    # Cols test cases start here
    def test_COLSInitialization(self):
        # Test case 1: Check if the class is initialized properly
        row = ["A", "b", "c"]
        cols = COLS(row)
        assert cols.x == {0: NUM("A", 0), 1: SYM("b", 1), 2: SYM("c", 2)}
        assert cols.y == {}
        assert cols.all == {0: NUM("A", 0), 1: SYM("b", 1), 2: SYM("c", 2)}
        assert cols.klass is None
        assert cols.names == ["A", "b", "c"]

        # Test case 2: Check if columns with "!+-" are added to self.x only
        row = ["A", "B!", "C"]
        cols = COLS(row)
        assert cols.x == {0: NUM("A", 0), 2: SYM("C", 2)}
        assert cols.y == {1: SYM("B!", 1)}
        assert cols.all == {0: NUM("A", 0), 1: SYM("B!", 1), 2: SYM("C", 2)}
        assert cols.klass is None
        assert cols.names == ["A", "B!", "C"]

        # Test case 3: Check if names ending with "X" are not taken
        row = ["A", "b!", "cX"]
        cols = COLS(row)
        assert cols.x == {0: NUM("A", 0)}
        assert cols.y == {1: SYM("b!", 1)}
        assert cols.all == {0: NUM("A", 0), 1: SYM("b!", 1), 2: SYM("cX", 2)}
        assert cols.klass is None
        assert cols.names == ["A", "b!", "cX"]     

    def test_COLS_add(self):
            
        row = ["A", "b!", "c+"]
        cols = COLS(row)

        # Test case: Check if col.add works
        new_row = ["D", "e!", "f+"]
        cols.add(new_row)
        assert cols.x == {0: NUM("A", 0), 3: NUM("d", 3)}
        assert cols.y == {1: SYM("b!", 1), 2: SYM("c+", 2),4: SYM("e!", 4), 5: SYM("f+", 5)}
        assert cols.all == {
            0: NUM("A", 0),
            1: SYM("b!", 1),
            2: SYM("c+", 2),
            3: NUM("D", 3),
            4: SYM("e!", 4),
            5: SYM("f+", 5),
        }
        assert cols.klass is None
        assert cols.names == ["A", "b!", "c+", "D", "e!", "f+"]  
    # Cols test cases end here

    # Tricks test cases start here
    def test_coerce_with_valid_input(self):
        result = tricks.coerce("42")
        self.assertEqual(result, 42)

    def test_coerce_with_invalid_input(self):
        result = tricks.coerce("invalid")
        self.assertEqual(result, "invalid")

    @unittest.mock.patch('builtins.open', unittest.mock.mock_open(read_data='1,2,3\n4,5,6\n'))
    def test_csv_parser(self):
        result = list(tricks.csv(file="example.csv"))
        expected_output = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(result, expected_output)
    # Tricks test cases end here

if __name__ == "__main__":
    unittest.main()
