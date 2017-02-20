from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

read1 = open("2010_final.csv")
read2 = open("stat7_sanitation.csv")


fo1 = read1.readlines()
fo2 = read2.readlines()

write1 = open("newcsv1.csv",'w')

i = 1
for line1 in fo1:
    split1 = line1.split(',')
    print i
    print split1[1]
    print "------------"
    i = i + 1
    for line2 in fo2:
        split2 = line2.split(',')
        if split1[1] == split2[0]:
            apnd1 = line1.rstrip('\n')+','+split2[1]+'\n'
            write1.write(apnd1)
            print split1[0]

read1.close()
read2.close()
write1.close()
        
       
       
            
            
        
