import math
def binary_search(array,val):
    f=0
    l=len(array)-1
    while(l>=f):
        mid=int((f+l)/2)
        if(array[mid]==val):
            return mid
        elif(val>array[mid]):
            f=mid+1
        else:
            l=mid-1
array=[12,68,46,21,98,50]
val=12
index=binary_search(array,val)
print(index)
