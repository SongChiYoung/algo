import sys
sys.setrecursionlimit(9999999)  

input = lambda: sys.stdin.readline().rstrip()

def solve(MAP, n):
    def check(MAP, x, y, n):
        if(x == -1 or y == -1 or x == n or y == n):
            return
        if(MAP[x][y] == 0):
            return
        MAP[x][y] = 0
        check(MAP, x, y-1, n)
        check(MAP, x, y+1, n)
        check(MAP, x-1, y, n)
        check(MAP, x+1, y, n)

    cnt = 0
    for x in range(n):
        for y in range(n):
            cur = MAP[x][y]
            if cur == 1:
                cnt += 1
                check(MAP, x, y, n)

    return cnt

N = int(input())

R = [[0]*N for i in range(N)]
G = [[0]*N for i in range(N)]
RG = [[0]*N for i in range(N)]
B = [[0]*N for i in range(N)]

MAP = []
for n in range(N):
    MAP.append(list(input()))

for x in range(N):
    for y in range(N):
        cur = MAP[x][y]
        if cur == "R":
            R[x][y] = 1
            RG[x][y] = 1
        elif cur == "G":
            G[x][y] = 1
            RG[x][y] = 1
        elif cur == "B":
            B[x][y] = 1

_R = solve(R,N)
_G = solve(G,N)
_RG = solve(RG,N)
_B = solve(B,N)

print(_R+_G+_B, _RG+_B)
