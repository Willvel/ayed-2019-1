from sys import stdin
def posi(mat,i,j):
    if j < len(mat[0]) and i < len(mat) and mat[i][j] == "0":
        return True
    else:
        return False
def nev(mat,res,c):
    a,b = 0,0
    for k in range(len(res)):
        i,j = res[k]
        mat[i][j] = "0"
        if posi(mat,i,j+1):
            a,b = i,j+1
        elif posi(mat,i+1,j):
            a,b = i+1,j
    mat[a][b] = "*"
    res = [(a,b)]
    if a != 0:
        rec(mat,a,b,c,res)
    else:
        print("Cantidad de caminos =",c)
def rec(mat,i,j,c,res):
    if i == len(mat)-1 and j == len(mat[i])-1:
        res.append((i,j))
        c= c+1
        for k in range(len(mat)):
            for l in range(len(mat[i])):
                print(mat[k][l], end= " ")
            print()
        print("camino #",c)
        nev(mat,res,c)
    else:
        if posi(mat,i,j+1):
            res.append((i,j))
            mat[i][j+1] = "+"
            rec(mat,i,j+1,c,res)
        elif posi(mat,i+1,j):
            mat[i+1][j] = "+"
            res.append((i,j))
            rec(mat,i+1,j,c,res)
        else:
            mat[i][j] = 0
            if len(res) == 0:
                print("total de caminos",c)
            else:
                mat[i][j] = "x"
                i,j = res[-1]
                rec(mat,i,j,c,res[0:-1])
def main():
    lisa = stdin.readline().strip()
    res = []
    mat  = []
    c = 0
    for i in range(len(lisa)-1):
        if lisa[i] != "[" and lisa[i] != "," and lisa[i] != " " and lisa[i] != "]":
            res.append(lisa[i])
        elif lisa[i] == "]":
            mat.append(res)
            res = []
    i,j = 0,0
    mat[0][0] = "*"
    rec(mat,i,j,c,res)
main()
