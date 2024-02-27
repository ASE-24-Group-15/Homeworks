from datetime import datetime
from logging import config
import src.config as config

def generateStats():
    print("date : ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("file : ", config.the.file)
    print("repeats : 20")

