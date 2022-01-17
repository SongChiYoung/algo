import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

def diff(x, y):
    #abs(x) < abs(y) true
    _x = pow(x)
    _y = pow(y)
    
    if _x == _y:
        return x < y
    return pow(x) < pow(y)

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    chk = -0.1 if num < 0 else 0.1
    num = abs(num)
    if(num == 0):
        if(heap):
            res = heapq.heappop(heap)
            rnd = round(res)
            if (res < rnd):
                print(-rnd)
            else:
                print(rnd)
        else:
            print(0)
    else:
        heapq.heappush(heap, num+chk)
