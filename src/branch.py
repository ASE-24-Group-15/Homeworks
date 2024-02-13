from src.data import DATA
from src.l import l

def branch():
    d = DATA("../data/auto93.csv")
    best, rest, evals = d.branch()
    print("best", l().o(best.mid().cells))
    print("rest", l().o(rest.mid().cells))
    print("evals",evals)
    
