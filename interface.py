import heatMap as hm
import numpy as np
import time
hm.REFRENCE_LENGTH = 999

###CSV file inputed to this function has the following properties:
#  4th column should be start;
#  9th column should be Cigar ###
input = "bamToDf.csv"
condition = 700 ## '=' + 'X' < condition will be discarded
lengthLimit = hm.REFRENCE_LENGTH ### by increasing you will get zero padding at the end of the heatMap
kinds= ['X','I','D'] #### list of Kind

start = time.time()
hMaps = hm.conditionedHeatMapGenerator(path = input, condition= condition, kinds= kinds)

####################### normalizing the heatMap #####################################
for kind in kinds:
    hMaps[kind] = hMaps[kind]/sum(hMaps[kind])
#####################################################################################


print("run time:",time.time()-start)
hm.CSVGenerator(hMaps,"heatMap.csv",kinds) 




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

