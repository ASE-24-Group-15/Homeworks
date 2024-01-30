import math
import random

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
    
    def shuffle(t):
        u = list(t)
        for i in range(len(u) - 1, 1, -1):
            j = random.randint(0, i)
            u[i], u[j] = u[j], u[i]
        return u
        
