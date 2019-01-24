from sys import stdin
def rec(lisa,val):
    for i in range(len(lisa)):
        num = lisa[i]
        for j in range(len(lisa)):
            num2 = lisa[j]
            if num*num2 > val and i != j:
                val = num*num2
    print(val)

def main():
    lisa = list(map(int,stdin.readline().strip().split()))
    val = 0
    maxi = 0
    rec(lisa,val)
main()
