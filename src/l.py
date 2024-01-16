import math

class l:
    def __init__(self):
        pass
    
    def rnd(self, n, ndecs= None):
        if not isinstance(n, (int, float)):
            return n
        
        if int(n) == n: 
            return n
        
        mult = 10 ** (ndecs or 2)
        return math.floor(n * mult + 0.5) / mult
        