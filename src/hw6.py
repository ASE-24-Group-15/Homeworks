from datetime import datetime
from logging import config
import random
from src.data import DATA
from src.l import l
import src.config as config

def generateStats():
    print("date : ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("file : ", config.the.file)
    print("repeats : 20")
    print("seed : ", config.the.seed)
    
    data = DATA(config.the.file)
    print("rows : ", len(data.rows))
    print("cols : ", len(data.cols.names[0]))
    print("names \t\t\t\t", '[' + ', '.join(["'" + item + "'" for item in data.cols.names[0]]) + ']' + "\t\td2h-")
    dataMid = data.mid()
    dataDiv = data.div()
    print("mid \t\t\t\t", '[' + ', '.join(["'" + str(l.rnd(2, item)) + "'" for item in dataMid.cells]) + ']' + "\t\t" + str(l.rnd(2, dataMid.d2h(data))))
    print("div \t\t\t\t", '[' + ', '.join(["'" + str(l.rnd(2, item)) + "'" for item in dataDiv.cells]) + ']' + "\t\t" + str(l.rnd(2, dataDiv.d2h(data))))
    print("#")
    
    #running smo9 20 times
    for i in range(20):
        _, best = data.gate(4, 9, 0.5)
        print("smo9 \t\t\t\t", '[' + ', '.join(["'" + str(item) + "'" for item in best[-1].cells]) + ']' + "\t\t\t\t" + str(l.rnd(2, best[-1].d2h(data))))
    
    print("#")
    
    #running any50
    for i in range(20):
        rand50 = random.sample(data.rows, 50)
        rows = sorted(rand50, key=lambda x: x.d2h(data))
        print("any50 \t\t\t\t", '[' + ', '.join(["'" + str(item) + "'" for item in rows[0].cells]) + ']' + "\t\t\t\t" + str(l.rnd(2, rows[0].d2h(data))))
        
    print("#")
    
    #all data
    bestRow = sorted(data.rows, key=lambda x: x.d2h(data))[0]
    print("100% \t\t\t\t", '[' + ', '.join(["'" + str(item) + "'" for item in bestRow.cells]) + ']' + "\t\t\t\t" + str(l.rnd(2, bestRow.d2h(data))))
    

def experimentTreatments():
    print("date : ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("file : ", config.the.file)
    print("repeats : 20")
    print("seed : ", config.the.seed)
    data = DATA(config.the.file)
    print("rows : ", len(data.rows))
    print("cols : ", len(data.cols.names[0]))