import sys
input = lambda: sys.stdin.readline().rstrip()
#I = 0
N = int(input())

def visit(x, N, MAP, VISIT):
    #global I
    row = MAP[x]
    if VISIT[x]:
        return row
    VISIT[x] = 1
    res = [0]*N
    for i in range(N):
        if row[i] == 1:
            r = visit(i, N, MAP, VISIT)
            #I += 1
            #print(x, I, r)
            for idx in range(N):
                res[idx] += r[idx]
    for i in range(N):
        MAP[x][i] = 1 if row[i] or res[i] else 0

    return MAP[x]

MAP = []

for i in range(N):
    MAP.append(list(map(int, input().split())))

for x in range(N):
    VISIT = [0]*N
    visit(x, N, MAP, VISIT)

for row in MAP:
    for v in row:
        print(v, end=" ")
    print()

