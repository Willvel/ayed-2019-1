from sys import stdin

def rec(a,b,lisa):
    pib = lisa[1]
    num = lisa[0]+lisa[1]
    if a == 1:
        mod = num%b
        print(num)
        print("mod =",mod)
    else:
        print(num)
        lisa = [pib,num]
        return rec(a-1,b,lisa)
    
def main():
    n = int(stdin.readline().strip())
    m = int(stdin.readline().strip())
    lisa = [0,1]
    rec(n-1,m,lisa)
main()
