import time
start=time.time()
a=[i for i in range(1000000000)]
b=[i for i in range(1000000000,2000000000)]
c=[]

for i in range (len(a)):
    c.append(a[i]+b[i])
print(time.time()-start)