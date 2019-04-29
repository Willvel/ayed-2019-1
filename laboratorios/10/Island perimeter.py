from sys import stdin
def rec(vari,po_i,po_j,con,j):
    print("mirar arriba")
    print(con-1,j)
    if j in po_j and con-1 in po_i:
        for k in range(len(po_j)):
            if po_j[k] == j and po_i[k] == con-1:
                vari[k] = vari[k]-1
                return vari,-1
    return vari,0
def main():
    lisa = 0
    con = 0
    ayud = [-1,1]
    po_i = []
    po_j = []
    vari =[]
    res = 0
    while lisa != [0]:
        lisa = list(map(int,stdin.readline().strip().split()))
        lisa.append(0)
        for j in range(len(lisa)-1):
            if lisa[j] == 1:
                val = 4
                vari,num = rec(vari,po_i,po_j,con,j)
                print("nume", num)
                print("val",val)
                val = val + num
                if j > 0:
                    print("adelante y atras")
                    for k in range(len(ayud)):
                        if lisa[j+ayud[k]] == 1:
                            print(val)
                            val = val-1
                elif j == 0 and lisa[j+1] == 1:
                    print("primero en la linea",con)
                    val = val-1
                po_i.append(con)
                po_j.append(j)
                vari.append(val)
                print(po_i)
                print(po_j)
                print(vari)
        con = con+1
    for i in range(len(vari)):
        res = res + vari[i]
    print(res)
main()
