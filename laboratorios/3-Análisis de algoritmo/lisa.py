from sys import stdin

def rec(n,lisa,a,m,ini):
    fin = len(lisa)
    mid = (fin-ini)//2
    if len(lisa) > 0:
        if lisa[0] > m:
            m = lisa[0]
        if lisa[0] < a:
            a = lisa[0]
        return rec(n,lisa[1:],a,m)
    else:
        print(a,m)
    

def main():
    n = int(stdin.readline().strip())
    lisa = list(map(int,stdin.readline().strip().split()))
    mini = 0
    maxi = 0
    ini = 0
    rec(n,lisa,mini,maxi,ini)
main()
