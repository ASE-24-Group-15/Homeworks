import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))

sys.path.insert(1, root_dir)

from src import num
from src import sym


def test_Num():
    num = num.Num()
    nums = [5, 5, 5, 5, 10, 10]
    for n in nums:
        num.add(n)
    return 40//6 == num.mid() and 2.581988897471611 == num.div()

def test_Sym():
    sym = sym.Sym()
    syms = ['s', 's', 'd', 'd', 's', 's']
    for s in syms:
        sym.add(s)
    return 's' == sym.mid and 0.9182958340544896 == sym.div()


    
