from src.data import DATA
from src.l import l

def eq_bons():
    l_instance = l()
    d = DATA("../data/auto93.csv")
    best, rest, _ = d.branch()
    LIKE = [row.cells for row in best.rows]
    HATE = l_instance.many(l_instance.shuffle(rest.rows), 3 * len(LIKE))

    def score(range):
        return range.score("LIKE", len(LIKE), len(HATE))
    
    t = []
    for col in d.cols.x.values():
        print("")
        for range in ranges1(col, {"LIKE": LIKE, "HATE": HATE}):
            l_instance.oo(range)
            t.append(range)
    
    t = l_instance.keysort(t, lambda a: score(a))
    max_score = score(t[0])
    print("\n#scores:\n")
    for v in l_instance.slice(t, 1, the["Beam"]):
        if score(v) > max_score * 0.1:
            print(l_instance.rnd(score(v)), l_instance.o(v))
    
    l_instance.oo({"LIKE": len(LIKE), "HATE": len(HATE)})
