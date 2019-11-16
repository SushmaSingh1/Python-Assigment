def divisible(v):
    a=[]
    for x in range(0,v+1):
        if(x%7==0 and x%5==0):
            yield(x)
v=int(input())           
n=divisible(v)
print(tuple(n))
