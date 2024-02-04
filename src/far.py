from src.data import DATA
from src.l import l

def far():
    d = DATA("../data/auto93.csv")
    a, b, distance = d.farapart(d)
    l_instance = l()
    print(f'far1: {l_instance.o(a)},\nfar2: {l_instance.o(b)}')
    print(f'distance = {distance}')