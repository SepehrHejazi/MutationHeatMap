import heatMap as hm
import numpy as np
hm.REFRENCE_LENGTH = 999

###CSV file inputed to this function has the following properties:
#  4th column should be start;
#  9th column should be Cigar ###
input = "bamToDf.csv"
condition = 700 ## '=' + 'X' < condition will be discarded
lengthLimit = hm.REFRENCE_LENGTH ### by increasing you will get zero padding at the end of the heatMap
kinds= ['X','I','D'] #### list of Kind

hMaps = hm.conditionedHeatMapGenerator(path = input, condition= condition, kinds= kinds)

####################### normalizing the heatMap #####################################
for kind in kinds:
    hMaps[kind] = hMaps[kind]/np.linalg.norm(hMaps[kind])
#####################################################################################

hm.CSVGenerator(hMaps,"heatMap.csv",kinds) 