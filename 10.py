class Reverselter():
    def __init__(self,list):
        for i in reversed(range(len(list))):
            print(list[i])            
list=[9,8,7,6,5,4,3,2,1]
Reverselter(list)
