import json
def supd(n):
    if len(n)>0:
        return int(n[0])+supd(n[1:])
    else:
        return 0
def rec(a):
    if len(a)> 1:
        a = str(supd(a))
        return rec(a)
    else:
        return a
# TODO Complete!
def super_digit(n, k):
    print(n,k)
    num = str(n)*k
    new = str(supd(num))
    res = int(rec(new))
    return res 
if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            k = test["k"]
            actual = super_digit(n, k)
            expected = test['result']
            assert actual == expected, f'Test {i} | n: {n} | k: {k} | expected: {expected}, actual: {actual}'
        print('OK!')
