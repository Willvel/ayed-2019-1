from sys import stdin
def countWays(a, b): 
    res = b
    mod = 1000000007 
    elm,var = 0,b  
    for i in range(2,a+1): 
        elm = var    
        var = res*(b-1)  
        var = var%mod    
        res = (elm+var)%mod  
    return res
def main():
    a = int(stdin.readline().strip())
    b = int(stdin.readline().strip())
    print(countWays(a, b))
main()
