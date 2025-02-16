#If you want to use a function inside another file, can use the Mod function
import printArr
import math #inbuilt in python
#Import the file and from the file call the method
printArr.printArr([1,2,3,4,5,6,7,8,9,10])

def squareRoot(num):
    return math.sqrt(num)

print(squareRoot(25))

printArr.lenArr([1,2,3,4,5,6,7,8,9,10])