def ReverseDigits(n):
     
    a  = list(str(n))
    a.reverse()
    strA = ''.join(a)
    return int(strA)

print(ReverseDigits(12345))
