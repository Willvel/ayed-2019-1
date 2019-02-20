from sys import stdin
def rec(lisa,n):
    lisa.sort()
    res = 0
    con = 0
    for i in range(len(lisa)):
        if lisa[i] < n and res < n:
            con = con+1
            res = res+lisa[i]
    print(con)
def main():
    lisa = list(map(int,stdin.readline().strip().split()))
    n = int(stdin.readline().strip())
    rec(lisa,n)
main()
