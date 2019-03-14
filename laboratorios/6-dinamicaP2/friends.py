from sys import stdin
def rec(can):
    lisa = [0 for k in range(can+1)]
    for i in range(can+1):
        if i <= 2:
            lisa[i] = i
        else:
            lisa[i] = lisa[i-1] + (i-1)*lisa[i-2]
    print(lisa[-1])
            
def main():
    can = int(stdin.readline().strip())
    rec(can)
main()
