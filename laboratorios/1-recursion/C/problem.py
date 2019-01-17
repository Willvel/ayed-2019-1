import json


# TODO Complete!
def has_more_vowels(s):
    let = s[0].lower()
    if len(s)>1:
        if let == "a" or let == "e" or let == "i" or let == "o" or let == "u":
            return 1+has_more_vowels(s[1:])
        else:
            return



        
        
        
    return False


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            s = test["s"]
            actual = has_more_vowels(s)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
