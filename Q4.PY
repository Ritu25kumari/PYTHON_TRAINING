n1=[]
for x in range(1200,1300):
    if(x%4==0) and (x%8==0) and (x%6!=0):
        n1.append(str(x))
        print (','.join(n1))