import sys

input = lambda: sys.stdin.readline().rstrip()
STACK = []
def solve(x, y, cost,  MAP, N, M):
    global STACK
    if(x < 0 or y < 0
       or x >= N or y >= M
       or (x==0 and y==0)
       ):
        return

    cur = MAP[x][y]
    if(cur == 0):
       return

    if((MAP[x][y]==1) or cur > cost):
        MAP[x][y] = cost
        STACK.append([x-1, y, cost+1])
        STACK.append([x, y-1, cost+1])
        STACK.append([x+1, y, cost+1])
        STACK.append([x, y+1, cost+1])
        #solve(x-1, y, cost+1, MAP, N, M)
        #solve(x, y-1, cost+1, MAP, N, M)
        #solve(x+1, y, cost+1, MAP, N, M)
        #solve(x, y+1, cost+1, MAP, N, M)


N, M = map(int, input().split())

MAP = []
for n in range(N):
    MAP.append(list(map(int,input())))

x=0
y=0
##solve(x+1, y, 2, MAP, N, M)
##solve(x, y+1, 2, MAP, N, M)
STACK.append([x+1, y, 2])
STACK.append([x, y+1, 2])

while STACK:
    x, y, c = STACK.pop()
    solve(x, y, c, MAP, N, M)

print(MAP[N-1][M-1])
