import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
user = [[] for i in range(N)]
kbn = [[999]*N for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    user[a].append(b)
    user[b].append(a)
    #if a < b:
    #    user[a].append(b)
    #else:
    #    user[b].append(a)

for i in range(N):
    kbn[i][i] = 0
    NEXT = []
    NEXT.extend(user[i])

    VISITED = set(range(N))

    cost = 0
    
    while VISITED:
        VISIT = NEXT
        NEXT = []
        cost += 1
        while VISIT:
            idx = VISIT.pop()
            if idx in VISITED:
                kbn[i][idx] = cost
                NEXT.extend(user[idx])
                VISITED.remove(idx)

mini = 999
res = 0
for i in range(N):   
    _sum = sum(kbn[i])
    if _sum < mini:
        mini = _sum
        res = i

print(res+1)
