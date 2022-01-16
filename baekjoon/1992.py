import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

MAP = []
for i in range(N):
    li = list(input())
    MAP.append(li)
#build MAP

def is_complit(x,y,step):
    if(step == 1):
        return MAP[x][y]
    
    cur = step//2

    ul = is_complit(x,y,cur)
    ur = is_complit(x,y+cur, cur)
    dl = is_complit(x+cur, y, cur)
    dr = is_complit(x+cur, y+cur, cur)

    if ul == ur == dl == dr and len(ul) == 1:
        return ul
    else:
        return "({}{}{}{})".format(ul, ur, dl, dr)

print("{}".format(is_complit(0,0,N)))
