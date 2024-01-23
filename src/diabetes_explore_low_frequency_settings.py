from learn import learn 
from data import DATA
import config
#Test on diabetes
def diabetes_explore_low_frequency_settings():
    print("#{:4s}\t{}\t{}".format("acc", "k", "m"))
    for k in range(4):
        config.the.k = k
        for m in range(4):
            config.the.m = m
            wme = {"acc": 0, "datas": {}, "tries": 0, "n": 0}
            DATA("../data/diabetes.csv", lambda data, t: learn(data, t, wme))
            print("{:5.2f}\t{}\t{}".format(wme["acc"] / wme["tries"], k, m))
