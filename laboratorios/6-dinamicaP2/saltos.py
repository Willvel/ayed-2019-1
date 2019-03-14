from sys import stdin
def rec(lisa, pos, res, vel):
    if pos < len(lisa) and lisa[pos]:
        res.append(pos)
        return rec(lisa, pos+vel-1, res, vel), rec(lisa, pos+vel, res, vel), rec(lisa, pos+vel+1, res, vel)
    else:
        if pos == len(lisa) and lisa[pos-1]:
            return True
        else:
            return False
def main():
    lisa = eval(stdin.readline().strip())
    vel = int(stdin.readline().strip())
    pos = int(stdin.readline().strip())
    res = []
    if rec(lisa, pos, res, vel):
        print("True")
    else:
        print("False")
main()
