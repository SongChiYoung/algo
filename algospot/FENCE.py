import sys
input = lambda : sys.stdin.readline().rstrip()

#if 0,1 mean, 0 to 0
def solve(fences, x, y):
    if(y-x <= 1):
        return fences[x]

    mid = (x+y)//2
   
    l = mid-1
    r = mid
    
    left = solve(fences, x, mid)
    right = solve(fences, mid, y)

    total = 0
    
    cur = min(fences[l],fences[r])
    cnt = 2
    total = cur*cnt

    while(1):
        if l <= x and r >= (y-1):
            #total = max(total, cur*cnt)
            break
        elif l <= x:
            cnt += 1
            r += 1
        elif r >= (y-1):
            cnt += 1
            l -= 1
        else:
            cnt += 1
            if fences[r+1] > fences[l-1]:
                r+=1
            else:
                l-=1

        cur = min(cur, fences[r], fences[l])
        total = max(total, cur*cnt)
    return max(total, left, right)

C = int(input())
for c in range(C):
    fences = []
    N = int(input())
    fences = list(map(int, input().split()))
    res = solve(fences, 0, len(fences))
    print(res)
