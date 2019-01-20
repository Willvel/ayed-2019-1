import json
def rec(s,con):
    if len(s)>0:
        let = s[0].lower()
        if let == "a" or let == "e" or let == "i" or let == "o" or let == "u":
            return rec(s[1:],con+1)
        else:
            return rec(s[1:],con)
    else:
        return con

# TODO Complete!
def has_more_vowels(s):
    con = 0
    num = int(rec(s,con))
    nvo = int(len(s)-rec(s,con))
    if num > nvo:
        return True
    else:
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
