from sys import stdin
def agreg(supr,piv,ayud):
    posi = []
    for i in range(len(supr)):
        var = supr[i]*piv
        if var not in supr and var not in ayud:
            posi.append(var)
    return posi
def main():
    num = int(stdin.readline().strip())
    lisa = list(map(int,stdin.readline().strip().split()))
    supr = [1]
    ayud = [(lisa[0])**2]
    while num > len(supr):
        if lisa != []:
            if ayud[0] < lisa[0]:
                piv = ayud[0]
                supr.append(ayud[0])
                ayud.remove(piv)
            elif ayud[0] > lisa[0]:
                piv = lisa[0]
                supr.append(lisa[0])
                lisa.remove(piv)
        else:
            le = num-len(supr)
            supr = supr+ayud[0:le]
        ayud = (ayud+agreg(supr,piv,ayud))
        ayud.sort()
    print(supr[-1])
            
main()
