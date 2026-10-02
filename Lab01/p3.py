def desc_cifre(x : int):
    #puts x's digits in an array , in a mirrored way
    cif = []
    while x > 0 :
        cif.append(x % 10)
        x //= 10
    return cif

def micsoreaza(n : int):
    #sorts n's digits in ascending order , forming a minimal number
    if n == 0:
        return 0

    rezultat = desc_cifre(n)
    rezultat.sort()

    if rezultat[0] == 0:
        i = 0
        while i < len(rezultat) and rezultat[i] == 0:
            i += 1
        if i < len(rezultat):
            rezultat[0], rezultat[i] = rezultat[i], rezultat[0]

    numar = 0
    i = 0
    while i < len(rezultat):
        numar = numar * 10 + rezultat[i]
        i += 1
    return numar

def read_nr() -> int:
    #reads the input from the console
    return int(input("Chose a number : "))

def output(n : int):
    #prints the answer on the console
    print(f"The minimal number formed from {n} is {micsoreaza(n)}")

def main():
    n = read_nr()
    output(n)

main()


