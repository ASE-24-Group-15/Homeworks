from src.tricks import csv
from src.row import ROW
from src.cols import COLS
from src.l import l
import src.config as config 
import random

class DATA:
    def __init__(self, src, fun = None):
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            for x in csv(src):
                self.add(x, fun)
        elif src is not None:
            for x in src:
                self.add(x, fun)
        
    def add(self, t, fun=None):
        row = t if not isinstance(t, list) and t.cells else ROW(t)
        if self.cols:
            if(fun):
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)
    
    def mid(self, cols=None):
        u = []
        for col in cols or self.cols.all.values():
            u.append(col.mid())
        return ROW(u)

    def stats(self, cols = None, fun = None, ndivs = None):
        u = {".N" : len(self.rows)}
        targetCols = getattr(self.cols, fun or "y")
        for col in targetCols:
            u[targetCols[col].txt] = l().rnd(getattr(targetCols[col], fun or "mid")(), ndivs)
        print(u)
        return u
    
    def gate(self, budget0, budget, some):
        stats, bests = [], []
        rows = l.shuffle(self.rows)
        row1 = []
        row2 = []
        row3 = []
        row4 = []
        row5 = []
        row6 = []
        
        row1 += [[row.cells[i] for i in list(self.cols.y.keys())] for row in rows[:6]]

        row2 += [[row.cells[i] for i in list(self.cols.y.keys())] for row in rows[:50]]

        rows.sort(key=lambda x: x.d2h(self))
        row3 += [[row.cells[i] for i in list(self.cols.y.keys())] for row in [rows[0]]]

        rows = l.shuffle(rows)
        lite = rows[:budget0]
        dark = rows[budget0:]

        for i in range(budget):
            best, rest = self.bestRest(lite, len(lite) ** some)
            todo, selected = self.split(best, rest, lite, dark) 

            sample = [self.cols.names[0][-len(self.cols.y.keys()):]] 
            random_sample = random.sample(dark, k=budget0+i)
            for d in random_sample:
                sample.append(d.cells[-len(self.cols.y.keys()):])
            rand_centroid = DATA(sample).mid() 
            row4.append(rand_centroid.cells)

            sample = [self.cols.names[0][-len(self.cols.y.keys()):]] 
            for d in selected.rows:
                sample.append(d.cells[-len(self.cols.y.keys()):])
            mid_centroid = DATA(sample).mid() 
            row5.append(mid_centroid.cells)

            # top_row_values = [[best.cells[i] for i in list(self.cols.y.keys())] for best in bests[:1]]

            dark.pop(todo)

            stats.append(selected.mid())
            bests.append(best.rows[0])
            lite.append(dark.pop(todo))
        
            row6.append(bests[0].cells[-len(self.cols.y.keys()):])

        return stats, bests, row1, row2, row3, row4, row5, row6
            
    def bestRest(self, rows, want):
        rows = sorted(rows, key=lambda x: x.d2h(self))
        best, rest = self.cols.names[:], self.cols.names[:]
        for i, row in enumerate(rows):
            if i < want:
                best.append(row)
            else:
                rest.append(row)
        return DATA(best), DATA(rest)
    
    def split(self, best, rest, lite, dark):
        selected = DATA(self.cols.names)
        max = 1E30
        out = 0
        for i, row in enumerate(dark):
            b = row.like(best, len(lite), 2)
            r = row.like(rest, len(lite), 2)
            if b > r :
                selected.add(row)
            tmp = abs(b+r) / abs(b -r + 1E-300)
            if tmp > max:
                out, max = i, tmp
        return out, selected
    
    def farapart(self, data, sortp=False, a=None):
        rows = data.rows or self.rows
        far = int(len(rows) *  config.the.get("Far", 0.95))
        evals = 1 if a else 2
        if not a:
            a = random.choice(rows).neighbors(self, rows)[far]
        b = a.neighbors(self, rows)[far]

        if sortp and b.d2h(self) < a.d2h(self):
            a, b = b, a

        return a, b, a.dist(b, self)

    



        