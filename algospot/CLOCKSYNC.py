import pprint
import time

import sys
input = lambda : sys.stdin.readline().rstrip()

buttons = [
    [0,1,2],
    [3,7,9,11],
    [4,10,14,15],
    [0,4,5,6,7],
    [6,7,8,10,12],
    [0,2,14,15],
    [3,14,15],
    [4,5,7,14,15],
    [1,2,3,4,5],
    [3,4,5,9,13]
]

#%% 
def clk_clock(btns, clk):
    for btn in btns:
        cur = clk[btn] + 3
        clk[btn] = cur%12
        #clk[btn] = cur if cur != 15 else 3
        #clk[btn] = clk_move(clk[btn])
    #return clk

def clk_move(now):
    now = now+3
    return now%12
    #if(now == 15):
    #    return 3
    #else:
    #    return now

def is_solved(clk):
    #return not sum(clk)
    #if max(clk):
    #    return 0
    #else:
    #    return 1
    for c in clk:
        if c:
            return 0
    else:
        return 1

def solve(clks, btn, click):
    if is_solved(clks):
        return click
    if (btn == 10):
        #print(clks)
        return 100
    
    mini = 100
    btns = buttons[btn]
    #for i in range(4):
    #    now = solve(clks, btn+1, click+i)
    #    mini = mini if mini < now else now
    #
    #    clk_clock(btns, clks)
    #    #print(clks)
    #    #ress.append(solve(clks, btn+1, click+i))
      
    now1 = solve(clks, btn+1, click+0)
    clk_clock(btns, clks)
 
    now2 = solve(clks, btn+1, click+1)
    clk_clock(btns, clks)

    now3 = solve(clks, btn+1, click+2)
    clk_clock(btns, clks)
 
    now4 = solve(clks, btn+1, click+3)
    clk_clock(btns, clks)

    mini = min((mini, now1, now2, now3, now4))

    return mini
        

    

T = int(input())
for t in range(T):
    #tmp = time.time()
    clks = list(map(int, input().replace("12","0").split()))
    res = solve(clks, 0, 0)
    if res == 100:
        print(-1)
    else:
        print(res)
    #print(time.time() - tmp)
