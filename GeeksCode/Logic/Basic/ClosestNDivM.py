
def mAndN(n, m):

    for i in range(1, m+1):

        b  = n - i
        f = n + i

        if (b % m == 0) and (f % m == 0):
            return b if abs(b) > abs(f) else f
        elif b % m == 0: 
            return b
        elif f % m == 0:
            return f



print(mAndN(-15, 6))
