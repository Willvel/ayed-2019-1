from sys import stdin
def rec(lisa,k,con):
    lisa.sort()
    if len(lisa) > 1:
        if lisa[0] <= k or lisa[1] <= k:
            val = (1*lisa[0]+2*lisa[1])
            lisa.append(val)
            print(lisa[2:])
            return rec(lisa[2:],k,con+1)
    if lisa[0] >= k:
        print(con)
    else:
        print("-1")
def main():
    a,k = map(int,stdin.readline().strip().split())
    lisa = list(map(int,stdin.readline().strip().split()))
    con = 0
    rec(lisa,k,con)
main()
