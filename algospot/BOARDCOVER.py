import sys
import pprint
import copy
input = lambda : sys.stdin.readline().rstrip()


DB = 1

"""def debug(x):
    return
    global DB
    print(DB)
    pprint.pprint(x, compact=False, width = 50)
    DB+=1"""

cases = [
    [[0,0],[0,1],[1,0]],
    [[0,0],[0,1],[1,1]],
    [[0,0],[1,0],[1,1]],
    [[0,1],[1,0],[1,1]]
]
"""
1 1
1
1 1
  1
1
1 1
  1
1 1
"""

def next(x, y, w, h):
    x = x+(y+1)//(w-1)
    y = (y+1)%(w-1) 
    return x,y

def isfull(mp):
    for row in mp:
#    row = mp[-1 ]
        for col in row:
            if(col == 0):
                return 0
    return 1

def set(mp, x, y, case, st):
    for a,b in case:
        a += x
        b += y 
        mp[a][b] += st    

def solve(mp, x, y, w, h):
    #print(x, y)
    if x == h-1:
        return isfull(mp)

    #mps = []
    sumd = mp[x][y] + mp[x][y+1] + mp[x+1][y] + mp[x+1][y+1]
    _x, _y = next(x, y, w, h)
    res = 0
    
    if mp[x][y] == 1:
        res += solve(mp, _x, _y, w, h)
        #mps.append(None)

    if sumd < 2:
        if sumd == 0:
            for case in cases[:3]:
                set(mp, x, y, case, 1)
                res += solve(mp, _x, _y, w, h)
                set(mp, x, y, case, -1)
            #_cases = cases[:3]
        else:
            if mp[x][y] == 1:
                set(mp, x, y, cases[3], 1)
                res += solve(mp, _x, _y, w, h)
                set(mp, x, y, cases[3], -1)
                #mps.append(case[3])
                #_cases = [cases[3]]
            elif mp[x][y+1] == 1:
                set(mp, x, y, cases[2], 1)
                res += solve(mp, _x, _y, w, h)
                set(mp, x, y, cases[2], -1)
                #_cases = [cases[2]]
            elif mp[x+1][y] == 1:
                set(mp, x, y, cases[1], 1)
                res += solve(mp, _x, _y, w, h)
                set(mp, x, y, cases[1], -1)
                #_cases = [cases[1]]
            else:
                set(mp, x, y, cases[0], 1)
                res += solve(mp, _x, _y, w, h)
                set(mp, x, y, cases[0], -1)
                #_cases = [cases[0]]  
        #for case in _cases:
        #    mps.append(case)

    #for case in mps:
    #    if case != None: set(mp, x, y, case, 1)
    #    res += solve(mp, _x, _y, w, h)
    #    if case != None: set(mp, x, y, case, -1)
    
    return res



T = int(input())

for t in range(T):
    H, W = map(int, input().split())
    mp = [[0]*W for i in range(H)]
    for h in range(H):
        row = input()
        for w in range(W):
            curr = row[w]
            if(curr == "#"):
                mp[h][w] = 1
            elif(curr == "."):
                mp[h][w] = 0
    #debug(mp)
    print(solve(mp, 0, 0, W, H))