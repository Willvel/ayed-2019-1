import json
def rec(par,impar,lisa):
    if len(lisa)>0:
        if lisa[0]%2==0:
            par.append(lisa[0])
            return rec(par,impar,lisa[1:])
        else:
            impar.append(lisa[0])
            return rec(par,impar,lisa[1:])
    num = par+impar
    print(num)
    return num
# TODO Complete!
def arrange(numbers):
    par = []
    impar=[]
    numbers = rec(par,impar,numbers)
    return numbers


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
