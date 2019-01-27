from sys import stdin

def mayor(lisa,can,new,cad):
    while len(lisa) > 0:
        if lisa[0] in new:
            val = new.index(lisa[0])
            cad[val] = cad[val]-1
            return mayor(lisa[1:],can,new,cad)
        else:
            new.append(lisa[0])
            cad.append(can-1)
            return mayor(lisa[1:],can,new,cad)
    if 0 in cad:
        print("True")
    else:
        print("False")
        
def main():
    num = int(stdin.readline().strip())
    lisa = list(map(int,stdin.readline().strip().split()))
    can = (num//2)+1
    new = []
    cad = []
    mayor(lisa,can,new,cad)

main()
