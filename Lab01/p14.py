def secventa(n: int):
    cnt = 0
    numar = 1                      # numar e numarul curent
    while True:                    # cnt , pe unde ne aflam in sir (index)
        if numar == 1:             #temp, folosit doar la descompunere , cu d
            cnt += 1               #marime ; cate nr afisez per pas
            if cnt == n:
                return 1
        else:
            temp = numar
            d = 2
            while temp > 1:
                if temp % d == 0:
                    while temp % d == 0:
                        temp //= d
                    if d == numar:
                        marime = 1
                    else:
                        marime = d
                    if n <= cnt + marime:      # elem. n apartine in intervalul asta
                        return d
                    cnt += marime
                d += 1
        numar += 1

print(secventa(1))
print(secventa(4))
print(secventa(12))