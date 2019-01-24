from sys import stdin

def rec(lisa,num,val):
    ini = 0
    fin = len(lisa)
    mid = (fin-ini)//2
    if len(lisa) == 1:
        if num == lisa[mid]:
            val = val+mid
            return val
        else:
            val = -1
            return val
    elif num == lisa[mid]:
        val = val+mid
        return val
    elif num > lisa[mid]:
        val = val+mid
        return rec(lisa[mid:fin],num,val)
    elif num < lisa[mid]:
        return rec(lisa[ini:mid],num,val)

def main():
    lisa = list(map(int,stdin.readline().strip().split()))
    num =int(stdin.readline().strip())
    val = 0
    print(rec(lisa,num,val))
main()
