def findNegativeAndPositive():
    length = int(input("Enter list's length: "))
    number = []
    negativeNum = []
    positiveNum = []
    for i in range(length):
        numberInput = int(input("Enter a number: "))
        number.append(numberInput)

    #check if the number is negative or positive
    for j in number:
        if j< 0:
            negativeNum.append(j)
        else :  positiveNum.append(j)

    #display negative and positive number
    print(f"Negative numbers : {negativeNum}")
    print(f"Negative numbers : {positiveNum}")

findNegativeAndPositive()
    
    
