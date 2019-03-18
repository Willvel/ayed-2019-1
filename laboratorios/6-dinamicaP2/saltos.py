from sys import stdin
def rec(lisa, pos, res, vel):
    print("posi",pos)
    if pos == len(lisa)-1 and lisa[pos]:
        print(res)
        return True
    elif pos < len(lisa)-1 and lisa[pos]:
        print("posible",pos)
        print("caminos",pos+vel-1,pos+vel,pos+vel+1)
        if pos not in res:
            res.append(pos)
        return rec(lisa, pos+vel-1, res, vel), rec(lisa, pos+vel, res, vel), rec(lisa, pos+vel+1, res, vel)
    else:
        print("no",pos)
        return False
def main():
    lisa = eval(stdin.readline().strip())
    vel = int(stdin.readline().strip())
    pos = int(stdin.readline().strip())
    res = []
    val = rec(lisa, pos, res, vel)
    if val:
        print("correcto",res)
    else:
        print("fail")
main()

