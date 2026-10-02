def desc_cifre(x : int):
    #puts x's digits in an array , in a mirrored way
    cif = []
    while x > 0 :
        cif.append(x % 10)
        x //= 10
    return cif

def micsoreaza(n : int):
    #sorts n's digits in ascending order
    rezultat = desc_cifre(n)
    rezultat.sort()
    numar = 0
    i = 0
    while i < len(rezultat):
        numar = numar * 10 + rezultat[i]
        i += 1
    return numar

def read_nr() -> int:
    #reads the input from the console
    return int(input("Chose a number : "))

def main():
    n = read_nr()
    print(f"The minimal number formed from {n} is {micsoreaza(n)}")

main()


