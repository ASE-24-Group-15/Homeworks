__doc__ = """
OPTIONS:
  -b --bins   initial number of bins      = 16
  -B --Bootstraps number of bootstraps    = 512
  -c --cohen  parametric small delta      = .35
  -C --Cliffs  non-parametric small delta = 0.2385 
  -f --file   where to read data          = "../data/auto93.csv"
  -F --Far    distance to  distant rows   = .925
  -g --go     start up action             = "help"
  -H --Half #examples used in halving   = 512
  -p --p      distance coefficient        = 2
  -S --seed   random number seed          = 1234567891
  -m --min    minimum size               = .5
  -r --rest   |rest| is |best|*rest        = 3
  -T --Top    max. good cuts to explore   = 10 
  -B --Beam   max number of ranges            = 10
"""
global the
the = {}