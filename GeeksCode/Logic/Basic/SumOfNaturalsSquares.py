
def SumOfNaturalsSqs(n):

    count = 0
    for i in range(1,n+1):
        sqr = i**2
        count += sqr
    
    print(count)


SumOfNaturalsSqs(8)
