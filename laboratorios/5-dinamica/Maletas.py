from sys import stdin
def best_case(peso_obj,maleta,elem,i,j):
    while i > 0:
        if peso_obj+maleta[i][j] == j or peso_obj+maleta[i][j] < j:
            return best_case(peso_obj,maleta,peso_obj+maleta[i][j],i-1,j)
        else:
            if peso_obj > maleta[i][j]:
                return best_case(peso_obj,maleta,peso_obj,i-1,j)
            else:
                return best_case(peso_obj,maleta,maleta[i][j],i-1,j)
    return elem      
def crea_male(cap_mal,obj):
    x = 0
    res = 0
    maleta = [[x+k for k in range(cap_mal+1)]]
    for i in range(len(obj)+1):
        if i == len(obj):
            peso_obj = obj[i-1]
        else:
            peso_obj = obj[i]
        lisa = []
        lisa.append(peso_obj)
        for j in range(cap_mal+1):
            elem = 0
            if peso_obj == j or peso_obj < j and i > 0:
                elem = best_case(peso_obj,maleta,elem,i,j)
                lisa.append(elem)
                if res < elem:
                    res = elem
            else:
                if peso_obj < j+1 or peso_obj == j+1:
                    lisa.append(peso_obj)
                else:
                    lisa.append(0)
            print(maleta[i][j], end = " ")
        print()
        maleta.append(lisa)
    return res
def main():
    obj =  list(map(int,stdin.readline().strip().split()))
    cap_m1 = int(stdin.readline().strip())
    cap_m2 = int(stdin.readline().strip())
    maleta_1 = crea_male(cap_m1,obj)
    print("1:",maleta_1)
    maleta_2 = crea_male(cap_m2,obj)
    print("2:",maleta_2)
    print(maleta_1+maleta_2)
main()
