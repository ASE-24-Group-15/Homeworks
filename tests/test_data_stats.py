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

import os
import subprocess
import sys
import ast
import unittest


class TestDataStatsScript(unittest.TestCase):
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


    

if __name__ == "__main__":
    unittest.main()