import numpy as np 

def fact(num):
    if num<=0:
        return 1
    return num*fact(num-1)

x = 0.2 
narr = np.zeros((5,6))
narr[:,0] = [0,1,2,3,4]
narr[:, 1] = [8,-1,-4,5,32] 

def delta():
    for i in range(2,6):
        for j in range(6-i):
            narr[j,i]=narr[j+1,i-1]-narr[j,i-1]

delta()
print(narr)


h = narr[1,0] - narr[0,0]
p = (x-narr[0,0])/h
y = (narr[0,1])


for i in range (1,5):
    y=y+(p*(narr[0,i+1]))/fact(i)
    print(y)
    p=p*(p-i)
    print(p)

print(y)



