from src.cols import COLS
import unittest

from src.num import NUM
from src.sym import SYM
from src.cols import COLS

class TestColsFunction(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()