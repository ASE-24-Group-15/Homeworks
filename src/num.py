class NUM:
    #Create
    def __init__(self, s= " ", n = 0):
        self.txt = s
        self.at = n
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1E30
        self.lo = 1E30
        self.heaven = s if (s or " ").endswith("−") else 1

        
    #Update
    def add(self, x):
        if x != "?":
            self.n = self.n + 1
            d = int(x) - self.mu
            self.mu = self.mu + (d / self.n)
            self.m2 = self.m2 + d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)
    
    #Query
    def mid(self):
        return self.mu
    
    def div(self):
        return 0 if self.n < 2 else (self.m2 / (self.n - 1)) ** 0.5

    #Likelihood
    def like(self, x):
        mu, sd = self.mid(), (self.div() + 1E-30)
        nom = 2.718 ** (-.5 * (x - mu) ** 2 / (sd ** 2))
        denom = (sd * 2.5 + 1E-30)
        return nom / denom
    
            