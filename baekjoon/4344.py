import sys
input = lambda: sys.stdin.readline().rstrip()

C = int(input())
for _ in range(C):
    cnt, *score = list(map(int, input().split()))
    avg = sum(score)/cnt
    num = 0
    for i in score:
        if avg < i:
            num += 1
    print("{:.3f}".format(num/cnt*100))
