from sys import stdin
def sencillo(dine, valor):
    x = 0
    cambio = [[x+k for k in range(dine+1)]]
    for i in range(len(valor)+1):
        if i == len(valor):
            preci = valor[i-1]
        else:
            preci = valor[i]
        lisa = []
        lisa.append(preci)
        for j in range(dine+1):
            cap_vu = j+1
            lisa.append(cap_vu//preci)
            print(cambio[i][j], end = " ")
        print()
        cambio.append(lisa)
    print("respuesta:",cambio[1][-1])
def main():
    dine = int(stdin.readline().strip())
    valor = list(map(int,stdin.readline().strip().split()))
    sencillo(dine, valor)
main()
