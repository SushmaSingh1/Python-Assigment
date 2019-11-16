list = [12,24,35,24,88,120,155,88,120,155]
dup=set(list)
uni=[]
for p in list:
    if (p in dup):
         uni.append(p)
         dup.remove(p)
print(uni)
