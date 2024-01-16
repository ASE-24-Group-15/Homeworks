from tricks import csv
from row import ROW
from cols import COLS
from l import l

class DATA:
    def __init__(self, src, fun):
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            for x in csv(src):
                self.add(x, fun)
        else:
            for x in src:
                self.add(x, fun)
        
    def add(self, t, fun):
        row = ROW(t)
        if self.cols:
            if(fun):
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)
    
    def stats(self, cols = None, fun = None, ndivs = None):
        u = {".N" : len(self.rows)}
        targetCols = getattr(self.cols, fun or "y")
        for col in targetCols:
            u[targetCols[col].txt] = l().rnd(getattr(targetCols[col], fun or "mid")(), ndivs)
        print(u)
        return u
        
        
        
