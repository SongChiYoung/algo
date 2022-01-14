import sys
input = lambda: sys.stdin.readline().rstrip()

class RES:
    m = 0
    p = 0
    z = 0

def solve(paper, x, y, cnt, res):
    if(cnt == 1):
        return paper[x][y]
    
    cur = cnt//3
    tmp = []
    for i in range(3):
        for j in range(3):
            tmp.append(solve(paper, x+(i*cur), y+(j*cur), cur ,res))

    m = tmp.count(-1)
    z = tmp.count(0)
    p = tmp.count(1)

    if(m == 9):
        return -1
    elif(z == 9):
        return 0
    elif(p == 9):
        return 1
    else:
        res.m += m
        res.p += p
        res.z += z
        return 999
 

N = int(input())

paper = []
for n in range(N):
    row = list(map(int, input().split()))
    paper.append(row)

res = RES()
ans = solve(paper,0,0,N,res)

if ans == -1:
    res.m += 1
elif ans == 0:
    res.z += 1
elif ans == 1:
    res.p += 1

print(res.m)
print(res.z)
print(res.p)

   
