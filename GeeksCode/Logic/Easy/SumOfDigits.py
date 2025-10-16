def SumOfDigits(n):
     
    a = list(str(n))
    total = 0
    for i in a:
        total += int(i)
    
    return total
    

print(SumOfDigits(12))
