from src.num import NUM
from src.sym import SYM

class COLS:
    #Create
    def __init__(self, row):
        klass, col = None, None
        self.x, self.y, self.all = {}, {}, {}
        for at, txt in enumerate(row['cells'], start=1):
            col = (NUM if txt[0].isalpha() and txt[0].isupper() else SYM)(txt, at)
            self.all.append(col)
            if not txt.endswith("X"):
                if txt.endswith("!"):
                    klass = col 
                (self.y if txt.endswith("!") or txt.endswith("+") or txt.endswith("-") else self.x)[at] = col
        self.klass = klass
        self.names = row['cells']
    
    #Update
    def add(self, row):
        for cols in [self.x.values(), self.y.values()]:
            for col in cols:
                col.add(row['cells'][col.at])
        return row