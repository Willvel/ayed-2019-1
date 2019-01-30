from sys import stdin
def orde(numeros):
    izq,mit,der=[],[],[]
    i = 0
    if len(numeros)>1:
        piv=numeros[0]
        while len(numeros) > i:
            if piv<numeros[i]:
                izq.append(numeros[i])
                i = i+1
            elif piv>numeros[i]:
                der.append(numeros[i])
                i = i+1
            else:
                mit.append(numeros[i])
                i = i+1
        return (orde(der)+mit+orde(izq))
    return numeros
def main():
    num=int(stdin.readline().strip())
    numeros=list(map(int,stdin.readline().strip().split()))
    lisa = orde(numeros)
    val = str(lisa)[1:-1]
    print(val)
main()
