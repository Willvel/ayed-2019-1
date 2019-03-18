from sys import stdin
def domin(num):
    lisa = [0] * (num + 1) 
    lis2 = [0] * (num + 1) 
    lisa[0],lisa[1] = 1,0
    lis2[0],lis2[1] = 0,1
    for i in range(2,num+1): 
        lisa[i] = lisa[i - 2] + 2*lis2[i-1] 
        lis2[i] =  lisa[i-1] + lis2[i-2] 
    return lisa[num]
def main():
    num =  int(stdin.readline().strip())
    print(domin(num))
main()
