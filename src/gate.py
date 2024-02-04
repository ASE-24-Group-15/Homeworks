
"""
OPTIONS:
  -b --bins   initial number of bins      = 16
  -B --Bootstraps number of bootstraps    = 512
  -c --cohen  parametric small delta      = .35
  -C --Cliffs  non-parametric small delta = 0.2385 
  -f --file   where to read data          = "../data/auto93.csv"
  -F --Far    distance to  distant rows   = .925
  -g --go     start up action             = "help"
  -h --help   show help                   = False
  -H --Halves #examples used in halving   = 512
  -p --p      distance coefficient        = 2
  -S --seed   random number seed          = 1234567891
  -m --min    minimum size               = .5
  -r --rest   |rest| is |best|*rest        = 3
  -T --Top    max. good cuts to explore   = 10 
"""

import os
import sys

# Adding project root directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

import ast
import argparse
from src.data import DATA
from src.diabetes import eg_bayes
from src.soybean import eg_km
from src.smo import gate20
from src.diabetes_explore_low_frequency_settings import diabetes_explore_low_frequency_settings
import src.config as config
from src.l import l
from src.dist import dist
from src.far import far

def coerce(x):
   try : return ast.literal_eval(x)
   except Exception: return x.strip()

def o(x): 
  return x.__class__.__name__ +"{"+ (" ".join([f"{k} : {v} ;" for k,v in sorted(x.items()) if k[0]!="_"]))+"}"

def argument_parser():

    parser = argparse.ArgumentParser(description='Command line options.')
    parser.add_argument('-b', '--bins', type=int, default=16, help='initial number of bins')
    parser.add_argument('-B', '--Bootstraps', type=int, default=512, help='number of bootstraps')
    parser.add_argument('-c', '--cohen', type=float, default=.35, help='parametric small delta')
    parser.add_argument('-C', '--Cliffs', type=float, default=.2385, help='non-parametric small delta')
    parser.add_argument('-f', '--file', type=str, default="../data/auto93.csv", help='where to read data')
    parser.add_argument('-F', '--Far', type=float, default=.95, help='distance to  distant rows')
    parser.add_argument('-g', '--go', type=str, default="help", help='start up action')
    # parser.add_argument('-h', '--help', type=bool, default=False, help='show help')
    parser.add_argument('-H', '--Halves', type=int, default=512, help='#examples used in halving')
    parser.add_argument('-p', '--p', type=int, default=2, help='distance coefficient')
    parser.add_argument('-S', '--seed', type=int, default=1234567891, help='random number seed')
    parser.add_argument('-r', '--rest', type=int, default=3, help='|rest| is |best|*rest')
    parser.add_argument('-t', '--todo', type=str, default="help", help='Start up action')
    parser.add_argument('-T', '--Top', type=int, default=10, help='max. good cuts to explore')
    parser.add_argument('-k', '--k', type=int, default=1, help='low class frequency kludge')
    parser.add_argument('-m', '--m', type=int, default=2, help='low attribute frequency kludge')
    return parser

class SLOTS(dict): 
  __getattr__ = dict.get
  __setattr__ = dict.__setitem__
  __repr__ = o

def main():
  args = argument_parser().parse_args()
  config.the = SLOTS(__doc__= __doc__, **vars(args))
  if config.the.todo == "stats":
    data = DATA(config.the.file, None)
    getattr(data, config.the.todo)()
  if config.the.todo == "diabetes":
    eg_bayes() 
  if config.the.todo == "diabetes-elfs":
    diabetes_explore_low_frequency_settings()
  if config.the.todo == "soybean":
    eg_km()
  if config.the.todo == "SMO":
    gate20()
  if config.the.todo == "dist":
    dist()
  if config.the.todo == "far":
    far()

if __name__ == "__main__":
  main()
  
