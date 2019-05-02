from sys import stdin
def main():
    num = int(stdin.readline().strip())
    mat = [[0 for i in range(num)] for j in range(num)]
    lisa = []
    cont = 0
    res = 0
    while cont < num:
        x,y = map(int,stdin.readline().strip().split())
        lisa.append((x,y))
        for i in range(cont):
            x2,y2 = lisa[i]
            dist = ((x2-x)**2)+((y2-y)**2)
            if dist in mat[i]:
                res = res+2
            mat[i][cont],mat[cont][i] = dist,dist           
        cont = cont+1
    print(res)
main()
