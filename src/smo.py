from src.l import l
from src.data import DATA
from src.row import ROW

def gate20():
  # print("#best, mid")
  BUDGET0 = 4
  BUDGET = 16   
  SOME = 0.5 
  for i in range(20):
    d = DATA("../data/auto93.csv")
    stats, bests = d.gate(BUDGET0, BUDGET, SOME, i+1)
    stat, best = stats[-1], bests[-1]
    print(l().rnd(best.d2h(d)), l().rnd(stat.d2h(d)))


