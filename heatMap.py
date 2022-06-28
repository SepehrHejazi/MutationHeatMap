x= """26S55=1D1=1X2=1D9=1X9=2D6=1D6=2D1X30=1D9=2X12=1X11=1X17=2I1=1X4=1D2=1D1X16=1X3=1D13=1X23=3X1=2I4X3=2D24=1D3X3=2I3=1X21=1X74=1X9=1X1=3X4=1X1=2D34=1X8=1D9=1D3=1X60=1D1=1X4=3D2=2X57=2X29=1X2=1X2=1X44=1X4=1X6=4D16=1D3=1X2=1D1=1D7=1D1X9=1D22=1X5=1X15=1X65=1D5=2D1=1D26=1D1=1X7=1I28=1I10=2D26=1X7=1X16=11S"""
import re
import csv 

REFRENCE_LENGTH = 999
HEATMAP = [0]*REFRENCE_LENGTH

def reader(file):
    rows = []
    f =  open(file)
    csv_reader = csv.reader(f, delimiter=',')   
    for row in csv_reader:
        rows.append(row)
    f.close()
    del (rows[0])
    return rows
"""row[3] is start; row[8] is Cigar"""

def CSV_GENERATOR(src,output_name,kind):
    header = ["Query_name", "Length of SeQ", "Sum", "Number of "+kind, "AVG"]
    output = open(output_name,"w+",newline="")
    scv_writer = csv.writer(output)
    rows = reader(src)
    scv_writer.writerow(header)
    for i in range(len(rows)):
        scv_writer.writerow(func(rows,i,rows[i][8],kind))
    output.close()

def cigarParser(cigar, kind,start):
    match = re.findall(r"([0-9]+)([A-G,I-R, T-Z,=]+)", cigar)
    output = []
    for i in range(start):
        output.append(0)
    for i in match:
        for k in range(int(i[0])):
            if i[1] == kind:
                output.append(1)
            else:
                output.append(0)
    return output
   

def heatMapGenerator(kind):
    
    rows = reader("")
    
    for row in rows:
        output = cigarParser(cigar = row[8], kind = kind, start = row[3])
        if len(output) < REFRENCE_LENGTH:
            for i in range(REFRENCE_LENGTH -len(output)):
                output.append(0)
        HEATMAP += output[0:999]
    print(HEATMAP)
        
        
                
        
    
        