from sys import stdin
def rec(mat,res,a):
    for i in range(len(mat)):
        if a == mat[i][0] or a == mat[i][1]:
            if a == mat[i][0] and mat[i][1] not in res:
                res.append(mat[i][1])
            elif mat[i][0] not in res:
                res.append(mat[i][0])
    return res
 
def main():
    n = int(stdin.readline().strip())
    matriz = []
    lisa = []
    res = []
    c = 0
    while n > 0:
        print("CASO",c)
        a,b = stdin.readline().strip().split()
        lisa.append(int(a))
        lisa.append(int(b))
        print("lisa",lisa)
        print(matriz)
        matriz.append(lisa)
        rec(matriz,res,int(b))
        rec(matriz,res,int(a))
        print("amigos",res)
        print(n,c)
        lisa = []
        n,c = n-1,c+1
        print("inicia ciclo")
        print("res",res)
        for i in range(len(res)):
            if int(a) != res[i] and int(b) != res[i]:
                rec(matriz,res,res[i])
        print("respuesta final =",len(res))
        res = []
main()
