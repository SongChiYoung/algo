import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

def solve(x,y,MAP, VISIT, n):
    if(x < 0 or y < 0):
        return False
    if(x >= n or y >= n):
        return False
    if(VISIT[x][y]):
        return False

    if(x == n-1 and y == n-1):
        return True
    
    VISIT[x][y] = 8
    move = MAP[x][y]

    #pprint(VISIT)
    VISIT[x][y] = 7
    
    #u = solve(x-move, y, MAP, VISIT, n) 
    d = solve(x+move, y, MAP, VISIT, n) 
    #l = solve(x, y-move, MAP, VISIT, n) 
    r = solve(x, y+move, MAP, VISIT, n) 

    VISIT[x][y] = 1

    return d or r
    
C = int(input())

for _ in range(C):
    n = int(input())
    MAP = []
    VISIT = [[0]*n for i in range(n)]
    for i in range(n):
        MAP.append(list(map(int,input().split())))

    if solve(0, 0, MAP, VISIT, n):
        print("YES")
    else:
        print("NO")

