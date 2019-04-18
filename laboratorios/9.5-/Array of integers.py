from sys import stdin
def rec(camp,lisa,nume,cont,caso):
    asp1 = max(lisa)
    asp2 = max(nume)
    print(camp)
    if cont == 1:
        camp.append(asp1)
        camp.append(asp2)
        print("--------------------------",asp1+asp2)
        lisa.remove(asp1)
        nume.remove(asp2)
        print(camp)
        print(lisa)
        print(nume)
        rec(camp,lisa,nume,cont+1,caso)
    elif cont < caso:
        sum1 = asp1+camp[1]
        sum2 = asp2+camp[0]
        print("asp",asp1,asp2)
        print("sumas",sum1,sum2)
        if sum1 > sum2:
            print("--------------------------",sum1)
            camp.append(asp1)
            lisa.remove(asp1)
            rec(camp,lisa,nume,cont+1,caso)
        elif sum1 < sum2:
            print("--------------------------",sum2)
            camp.append(asp2)
            nume.remove(asp2)
            rec(camp,lisa,nume,cont+1,caso)
        else:
            print("--------------------------",sum1)
            print("--------------------------",sum2)
            camp.append(asp1)
            camp.append(asp2)
            lisa.remove(asp1)
            nume.remove(asp2)
            rec(camp,lisa,nume,cont+2,caso)
def main():
    lisa = list(map(int,stdin.readline().strip().split()))
    nume = list(map(int,stdin.readline().strip().split()))
    caso = int(stdin.readline().strip())
    camp = []
    cont = 1
    rec(camp,lisa,nume,cont,caso+1)
main()
