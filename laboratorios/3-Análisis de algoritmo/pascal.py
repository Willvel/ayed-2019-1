from sys import stdin

def fibo(n,lisa,res):
    if n > 0:
        if len(lisa) > 1:
            val = lisa[0]+lisa[1]
            res.append(val)
            fibo(n,lisa[1:],res)
        else:
            res.append(1)
            print(res)
            lisa = res
            res = [1]
            fibo(n-1,lisa,res)
            
def main():
    n = int(stdin.readline().strip())
    lisa = [1]
    res = []
    fibo(n,lisa,res)
main()
