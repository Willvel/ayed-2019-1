import json


# TODO Complete!!
def reverse(text):
    if len(text) == 1:
        return text[0]
    else:
        return text[-1]+reverse(text[:-1])

if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            text = test["text"]
            actual = reverse(text)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
