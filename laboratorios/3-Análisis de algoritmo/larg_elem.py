from sys import stdin

def invr(lisa):
    for j in range(1, len(lisa)):
        key = lisa[j]
        i = j
        while i > 0 and lisa[i-1] < key:
            lisa[i] = lisa[i-1]
            i = i-1
        lisa[i] = key
    print(lisa[0:10])
    
def main():
    lisa = list(map(int,stdin.readline().strip().split()))
    if len(lisa) > 10 or len(lisa)== 10:
        invr(lisa)
    else:
        print(lisa)
main()
