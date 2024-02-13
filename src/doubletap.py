from src.data import DATA
from src.l import l

def doubletap():
    d = DATA("../data/auto93.csv")
    best1, rest, evals1 = d.branch(32)
    best2, _, evals2 = best1.branch(4)
    print("best2", l().o(best2.mid().cells))
    print("rest", l().o(rest.mid().cells))
    print("evals", evals1 + evals2)
