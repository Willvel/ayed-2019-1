from sys import stdin
def main():
    lisa = list(map(int,stdin.readline().strip().split()))
    lisa.append(lisa[-1])
    can = 0
    dif = 0
    elm = lisa[-1]
    for i in range(len(lisa)-1):
        can = can+i
        dif = dif + abs(lisa[i]-lisa[i+1])
    if dif == can:
        print("True")
    else:
        print("False")
main()
