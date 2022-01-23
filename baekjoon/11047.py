import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(int(input()))

coin = coin[::-1]

res = 0
for c in coin:
    r = K//c
    res += r
    K -= c*r

print(res)
