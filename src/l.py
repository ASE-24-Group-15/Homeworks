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
    
    def o(self,t, n=None):
        if isinstance(t, (int, float)):
            return str(self.rnd(t, n))
        if not isinstance(t, dict) and not isinstance(t, list):
            return str(t)
        u = []
        for k, v in sorted(t.items()) if isinstance(t, dict) else enumerate(t):
            if str(k)[0] != "_":
                if len(t) > 0:
                    u.append(self.o(v, n))
                else:
                    u.append(f"{self.o(k, n)}: {self.o(v, n)}")
        return "{" + ", ".join(u) + "}"
        
