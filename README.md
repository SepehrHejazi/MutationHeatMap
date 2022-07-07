


reader returns an array that every elements is the row in the input file
every row has different 

file= 'bamToDf.csv'

print(hm.reader(file)[943])
output -> ['943', '48ece448-3179-4b65-af7d-bbd0be085fbb', 'referenceSequence_LET_sfGFP', '0', '987', '34', '1005',
            '0', '34S20=2X166=1X60=1D1=4D134= ...', 'ATACCTTTACGCGTTCCAGTTACGTAT ...', '60']




cigar = '1S2D3=1D2I1S'  # row[8]
kind  = 'D'  
start = 0               # int(row[3])
lengthLimit = 25        # This is the limit if cigar lengths are not the same, very big length limit will 
                          create zero adding at the end

cigarParser(cigar, kind,start,lengthLimit)
output -> [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

lengthLimit = 3
cigarParser(cigar, kind,start,lengthLimit)
output -> [1, 1, 0]







row = [0 for _ in range(9)]
row[3] = 0
row[8] = cigar

kinds = ['X','I','D']
print(hm.heatMapGenerator(kinds, row,lenghtLimit = 5))
output -> {'X': [0, 0, 0, 0, 0], 'I': [0, 0, 0, 0, 0], 'D': [1, 1, 0, 0, 0]}









path = 'bamToDf.csv'
REFRENCE_LENGTH = 5 # DNA refrence Length
kinds= ['X','I','D']
condition = 1 # will not include cigars if the number of 'X' and '=' are less than condition

conditionedHeatMapGenerator(path,condition = 0,lengthLimit = REFRENCE_LENGTH,kinds= ['X','I','D']):

output -> {'X': array([ 0,  0,  0,  2,  1, 12, 20,  8, 20, 38]), 'I': array([ 0,  0,  0,  0,  0,  0,  3, 16,  5, 13]), 'D': array([ 0,  0,  0,  0,  0,  0,  5, 12,  5,  9])}

