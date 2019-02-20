from sys import stdin
def main():
    n = int(stdin.readline().strip())
    lisa = [int(x) for x in stdin.readline().strip().split()]
    c = True 
    for i in range(len(lisa)):
        n = lisa[i]
        for j in range(2,n):
            if n%j == 0 and j < n-1:
                c = False
        if c:
            print("Si")
        else:
            print("No")
        c = True
main()
