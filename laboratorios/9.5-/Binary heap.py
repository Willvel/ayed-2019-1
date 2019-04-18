from sys import stdin
def rec(lisa,pa,c):
    pa.append(lisa[0])
    lisa.pop(0)
    if len(lisa) == 0:
        print("True")
    elif pa[0] > lisa[0] and c < 2:
        return rec(lisa,pa,c+1)
    elif c == 2:
        pa.pop(0)
        c = 0
        return rec(lisa,pa,c)
    else:
        print("False")
def main():
    lisa =list(map(int,stdin.readline().strip().split()))
    pa = []
    c = 0
    rec(lisa,pa,c)
main()
