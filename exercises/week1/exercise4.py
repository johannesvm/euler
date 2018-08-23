
def factorize(n):
    f = []
    p = 2
    while n >= p:
        if n % p == 0:
            f.append(p)
            if n/p == 1:
                break;
            n = n/p
        else:
            p += 1
    return f  
