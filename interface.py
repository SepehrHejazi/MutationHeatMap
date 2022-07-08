from importlib.resources import path
from posixpath import split
import heatMap as hm
import numpy as np
import time ,os
hm.REFRENCE_LENGTH = 999


#this method returns all CSV files in the current working directry
def getCSVInputs(workingDirectory = None):
    if workingDirectory is None:
        workingDirectory = os.getcwd()
    files = os.listdir(workingDirectory)
    CSVInputs = []
    for file in files:
        if file.endswith('.csv'):
            CSVInputs.append(file)
    X= input(str(CSVInputs)+"\nDoes this look good? \nPress any button to continue!\n OR choose the Indexes seperated by commo to continue!")
    if X == '':
        return CSVInputs
    else:
        CSVInputsMod = []
        for x in X.split(','):
            CSVInputsMod.append(CSVInputs[int(x)])
            input(str(CSVInputs)+"\nDoes this look good? \nPress any button to continue!")
            return CSVInputsMod

###CSV file inputed to this function has the following properties:
#  4th column should be start;
#  9th column should be Cigar ###






def heatMapGeneration(path):
    condition = 700 ## '=' + 'X' < condition will be discarded
    lengthLimit = hm.REFRENCE_LENGTH ### by increasing you will get zero padding at the end of the heatMap
    kinds= ['X','I','D'] #### list of Kind
    start = time.time()
    hMaps = hm.conditionedHeatMapGenerator(path = path, condition= condition, kinds= kinds)

    ####################### normalizing the heatMap #####################################
    for kind in kinds:
        #hMaps[kind] = hMaps[kind]/sum(hMaps[kind])
        hMaps[kind] = hMaps[kind]/np.linalg.norm(hMaps[kind],ord=1)
    #####################################################################################
    print("run time:",time.time()-start)
    hm.CSVGenerator(hMaps,"heatMap"+path,kinds) 
    return hMaps





CSVInputs = getCSVInputs()
cnt = 1
for csv in CSVInputs:
    print("Generating heatmap for "+ csv +". \nStep "+str(cnt)+" out of "+str(len(CSVInputs)))
    heatMapGeneration(csv)
    cnt +=1









#####################test cases!
# file= 'bamToDf.csv'
# print(hm.reader(file)[943])

# cigar = '1S2D3=1D2I1S'
# print(hm.cigarToHeatMap(cigar,'D',0,25))

# row = [0 for _ in range(9)]
# row[3] = 0
# row[8] = cigar
# kinds = ['X','I','D']
# print(hm.heatMapGenerator(kinds, row,5))

# print(hm.conditionedHeatMapGenerator(file,condition = 0,lengthLimit=10))

