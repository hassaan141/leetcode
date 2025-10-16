
def SwapTwoNums(a, b): # functions that are passed in are local copies

    a, b = b, a
    return a, b



a = 8
b = 6

print(a, b)
a, b = SwapTwoNums(a, b)
print(a,b)

#Look into a bitwise solution
