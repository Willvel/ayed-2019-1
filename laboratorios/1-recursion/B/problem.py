import json
global par, impar
par = []
impar =[]
def app(lis,num):
    lis.append(num)
# TODO Complete!
def arrange(numbers):
    global par,impar
    if len(numbers) > 1:
        if numbers[0]%2 == 0:
            app(par,numbers[0])
            return(numbers[1:])
        else:
            app(impar,numbers[0])
            return(numbers[1:])
    numbers = par+impar
    print(numbers)
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
