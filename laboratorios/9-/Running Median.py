from sys import stdin
def main():
    num_c = int(stdin.readline().strip())
    lisa = []
    while num_c > 0:
        cas_n = int(stdin.readline().strip())
        lisa.append(cas_n)
        lisa.sort()
        if len(lisa)%2 == 0:
            elm1 = lisa[len(lisa)//2]
            elm2 = lisa[(len(lisa)//2)-1]
            print(float((elm1+elm2)/2))
        else:
            print(float(lisa[len(lisa)//2]))
        num_c = num_c-1
main()
