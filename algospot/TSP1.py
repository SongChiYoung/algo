import sys
import pprint
input = lambda : sys.stdin.readline().rstrip()

DB = 0
def debug(x):
    global DB
    print(DB)
    pprint.pprint(x, compact=False, width = 50)
    DB+=1

def travel(dots, leng, visited, curr):
    N = len(dots)
    if(len(visited) == N):
        return leng#+ dots[curr][0]
    
    li = []
    for i in range(0, N):
        if i in visited:
            pass
        else:
            visited.add(i)
            li.append(travel(dots, leng, visited, i)+dots[curr][i])
            #print(visited, curr, i, li)
            visited.remove(i)
    return min(li)


T = int(input())
for t in range(T):
    N = int(input())
    dots = []
    for n in range(N):
        dots.append(list(map(float, input().split())))
    leng = []
    visited = set()
    for i in range(0,N):
        visited.add(i)
        leng.append(travel(dots, 0, visited, i))
        visited.remove(i)
    print(min(leng))

