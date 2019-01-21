import json
def cambio(num,ori,des,mid):
    if num >= 1:
        cambio(num-1,ori,mid,des)
        impre(ori,des)
        cambio(num-1,mid,des,ori)
def impre(a,b):
    print("mover disco de",a,"a",b)
# TODO Complete!
def hanoi(n):
    num = n
    ori = "A"
    des = "B"
    mid = "C"
    cambio(num,ori,des,mid)
if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            hanoi(n)
        print('OK!')
