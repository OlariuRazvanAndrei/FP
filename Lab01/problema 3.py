def desc_cifre(x : int):
    cif = []
    while x > 0 :
        cif.append(x % 10)
        x //= 10
    return cif

def micsoreaza(n : int):
    rezultat = desc_cifre(n)
    rezultat.sort()
    numar = 0
    i = 0
    while i < len(rezultat):
        numar = numar * 10 + rezultat[i]
        i += 1
    return numar

print(micsoreaza(98765))
print(micsoreaza(113))
print(micsoreaza(10))
print(micsoreaza(12034))
