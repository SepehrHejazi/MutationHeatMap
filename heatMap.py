# x= """26S55=1D1=1X2=1D9=1X9=2D6=1D6=2D1X30=1D9=2X12=1X11=1X17=2I1=1X4=1D2=1D1X16=1X3=1D13=1X23=3X1=2I4X3=2D24=1D3X3=2I3=1X21=1X74=1X9=1X1=3X4=1X1=2D34=1X8=1D9=1D3=1X60=1D1=1X4=3D2=2X57=2X29=1X2=1X2=1X44=1X4=1X6=4D16=1D3=1X2=1D1=1D7=1D1X9=1D22=1X5=1X15=1X65=1D5=2D1=1D26=1D1=1X7=1I28=1I10=2D26=1X7=1X16=11S"""
from importlib.resources import path
import re
import csv 
import numpy as np
from numpy import insert

REFRENCE_LENGTH = 999

def reader(file):
    rows = []
    f =  open(file)
    rows = csv.reader(f, delimiter=',')
    rows = list(rows)   
    del (rows[0])
    return rows ### row[3] is start; row[8] is Cigar



def cigarParser(cigar, kind,start):
    start = int(start)
    matches = re.findall(r"([0-9]+)([A-G,I-R, T-Z,=]+)", cigar)
    # matches is a list of tuple and each tuple is like ('22','D')#
    
    output = []
    for i in range(start):
        output.append(0)
    
    for match in matches:
        for k in range(int(match[0])): # for k in range(22):
            if match[1] == kind:            # if 'D' == kind:
                output.append(1)
            else:
                output.append(0)
    return output
   

def heatMapGenerator(kinds, row,lengthLimit):
    ## checking the condition:
    hMap = {kind: None for kind in kinds}
    for kind in kinds:
        hMap[kind] = cigarParser(cigar = row[8], kind = kind, start = row[3])
        hMap[kind] = hMap[kind][0:lengthLimit]
        if len(hMap[kind]) < lengthLimit:
            hMap[kind] += [0 for _ in range(lengthLimit-len(hMap[kind]))]
    return hMap

def conditionedHeatMapGenerator(path,condition = 700,lengthLimit = REFRENCE_LENGTH,kinds= ['X','I','D']):
    hMaps = {kind: [0 for _ in range(lengthLimit)] for kind in kinds}
    rows = reader(path)
    for row in rows:
        hMap = heatMapGenerator(kinds = kinds+['='], row = row ,lengthLimit = lengthLimit)
        if sum(hMap['=']) + sum(hMap['X']) > condition:
            for kind in kinds:
                hMaps[kind] = np.add(hMaps[kind], hMap[kind])
    return hMaps
def CSVGenerator(dict,output_name,kinds):
    output = open(output_name,"w+",newline="")
    writer = csv.writer(output)
    for kind in kinds:
        dict[kind] = list(dict[kind])
        dict[kind].insert(0,kind)
        writer.writerow(dict[kind])
    output.close()      



        
        
    
        