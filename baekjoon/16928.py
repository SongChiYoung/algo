import math
import sys
input = lambda: sys.stdin.readline().rstrip()

N,M = map(int, input().split())
NM = N+M

cost = math.ceil(100/6)

costs = [cost+3]*(101)
ways = list(range(101))#[0]*(101)

for i in range(NM):
    start, end = map(int, input().split())
    ways[start] = end

stk = [[1, 0]]
#cur, cost

while stk:
    cur, cost = stk.pop()
    for i in range(1,7):
        now = cur+i
        if now > 100:
            break
        end = ways[now]
        val = costs[end]

        new_val = (cost + 1)

        if new_val < val:
            costs[now] = new_val
            costs[end] = new_val
            stk.append([end, new_val])

print(costs[-1])

