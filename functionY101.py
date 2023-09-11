#create a list 

def createList():
    x = []
    length = int(input(" Enter list's length :"))
    
    for i in range(length):
        e = int(input())
        x.append(e)
    print(x)


createList()

