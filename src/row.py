import math
import src.config as config

class ROW:
    def __init__(self, t):
        self.cells = t

    # Return the ‘data‘ (from ‘datas‘) that I like the best
    def likes(self, datas):
        n, nHypotheses = 0, 0
        for k, data in datas.items():
            n += len(data.rows)
            nHypotheses += 1
        most = None
        out = None
        for k, data in datas.items():
            tmp = self.like(data, n, nHypotheses)
            if most == None or abs(tmp) > abs(most):
                most, out = tmp, k
        return out, most

    # How much does ROW like `self`. Using logs since these 
    # numbers are going to get very small.
    def like(self, data, n, nHypotheses):
        prior = (len(data.rows) + config.the.k) / (n + config.the.k * nHypotheses)
        out = math.log(prior)
        for col in data.cols.x.values():
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                if abs(inc) != 0:
                    out = out + math.log(inc)
                else:
                    out = out  +  float('-inf')
        return math.exp(1) ** out