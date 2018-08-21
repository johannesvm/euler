
def factorize(n):
    f = []
    p = 2
    while n >= p:
        if n % p == 0:
            print(f, n, p)
            f.append(p)
            if n/p == 1:
                break;
            n = n/p
        else:
            p += 1
            while True:
                if p % 2 == 0:
                    p += 1
                else:
                    break;
    return f

a = factorize(29)
print(a)
            
