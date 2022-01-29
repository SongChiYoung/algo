import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
apps = []

for _ in range(N):
    row = list(map(int, input()))
    apps.append(row)

stack = []
stack.append([0,0])
curr = [0,0]
cnt = 0
now = 0
lst = []
while stack:
    x,y = stack.pop()
    if x >= N or y >= N or x < 0 or y < 0: 
        continue
    elif apps[x][y] == 0:
        pass
    else:
        #print(x, y)
        apps[x][y] = 0
        now = 1
        cnt += 1

        if not(x-1 >= N or y >= N or x-1 < 0 or y < 0): 
            stack.append([x-1,y])
        if not(x >= N or y-1 >= N or x < 0 or y-1 < 0): 
            stack.append([x,y-1])
        if not(x+1 >= N or y >= N or x+1 < 0 or y < 0): 
            stack.append([x+1,y])
        if not(x >= N or y+1 >= N or x < 0 or y+1 < 0): 
            stack.append([x,y+1])

    if not stack:
        #print("t")
        def curr_go(curr):
            x,y = curr
            if x == N-1 and y == N-1:
                curr = []
            elif y == N-1:
                curr = [x+1, 0]
            else:
                curr = [x, y+1]
            return curr
        curr = curr_go(curr)
        if curr:
            stack.append(curr)
        if now:
            lst.append(cnt)
        now = 0
        cnt = 0
 

print(len(lst))
lst.sort()
for i in lst:
    print(i)
