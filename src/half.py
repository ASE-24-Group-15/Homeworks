from src.data import DATA
from src.l import l

def half():
    d = DATA("../data/auto93.csv")
    lefts, rights, left, right, C, cut, _ = d.half(d.rows)
    o = l().o
    print("lefts len", o(len(lefts)))
    print("rights len", o(len(rights)))
    print("left cells", o(left.cells))
    print("right cells", o(right.cells))
    print("Distance", o(C))
    print("cut", o(cut))

    
