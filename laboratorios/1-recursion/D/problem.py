import json
def rec(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return rec(n-1)+rec(n-2)+rec(n-3)
#TODO Complete!
def compute_ways(n):
    return rec(n)
if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            actual = compute_ways(n)
            expected = test['result']
            assert actual == expected, f'Test {i} | n: {n} | expected: {expected}, actual: {actual}'
        print('OK!')
