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
        
    # Return any item from `t`
    def any(self, t):
        return random.choice(t)

    # Return any `n` items (there may be repeats)
    def many(self, t, n):
        n = n or len(t)
        u = []
        for _ in range(n):
            u.append(random.choice(t))
        return u

    # Schwartzian transform:  decorate, sort, undecorate
    def keysort(self, t, fun):
        u = [{'x': x, 'y': fun(x)} for x in t]  # decorate
        u.sort(key=lambda a: a['y'])  # sort
        v = [xy['x'] for xy in u]  # undecorate
        return v


