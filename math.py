# Sample code

nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))



nl=[]
for x in range (1200, 1900):
    if (x%20==0) and (x%35==0):
        nl.append(str(x))
        print (','.join(nl))