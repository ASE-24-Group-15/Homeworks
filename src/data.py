from src.tricks import csv
from src.row import ROW
from src.cols import COLS
from src.l import l
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

        with open('gate20_output', 'a') as output_file:
            print("1. top6", [[row.cells[i] for i in list(self.cols.y.keys())] for row in rows[:6]] , file=output_file)
            print("2. top50", [[row.cells[i] for i in list(self.cols.y.keys())] for row in rows[:50]], file=output_file)

            rows.sort(key=lambda x: x.d2h(self))
            print("3. most", [[row.cells[i] for i in list(self.cols.y.keys())] for row in [rows[0]]], file=output_file)

            rows = l.shuffle(rows)
            lite = rows[:budget0]
            dark = rows[budget0:]

            for i in range(budget):
                best, rest = self.bestRest(lite, len(lite) ** some)
                todo, selected = self.split(best, rest, lite, dark) 

                rand_centroid = self.calculate_centroid(random.sample(dark, k=budget0+i)) 
                print(f"4: rand {rand_centroid}", file=output_file)

                mid_centroid = self.calculate_centroid(selected.rows)
                print(f"5: mid {mid_centroid}", file=output_file)

                top_row_values = [[best.cells[i] for i in list(self.cols.y.keys())] for best in bests[:1]]
                print(f"6: top: {top_row_values}", file=output_file)

                dark.pop(todo)

                stats.append(selected.mid())
                bests.append(best.rows[0])
                lite.append(dark.pop(todo))
        return stats, bests
            
            
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
    
    
    def calculate_centroid(self, data):
        last_n_elements = [d.cells[-len(self.cols.y.keys()):] for d in data]
        centroid = [sum(x) / len(x) for x in zip(*last_n_elements)]
        return centroid



        