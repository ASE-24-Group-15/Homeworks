from src.l import l
from src.data import DATA

def gate20():
  # print("#best, mid")
  for i in range(20):
    d = DATA("../data/auto93.csv")
    stats, bests = d.gate(4, 16, .5)
    stat, best = stats[-1], bests[-1]
    print(l().rnd(best.d2h(d)), l().rnd(stat.d2h(d)))