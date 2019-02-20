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
def rec(li,po,c):
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            elm = li[i]
            cor = po.index(elm)
            print(li)
            li[cor],li[i] = li[i],li[cor]
            print("cambio ",po[cor],"por",li[i])
            print(li)
            print("_____________________________________________")
            return rec(li,po,c+1)
    print(po)
    print("RESPUESTA =",c)
def main():
    lisa = list(map(int,stdin.readline().strip().split()))
    posi = orde(lisa)
    c = 0
    rec(lisa,posi,c)
main()
