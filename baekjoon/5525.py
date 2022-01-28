import sys
input = lambda: sys.stdin.readline().rstrip()

base = "I"
pad = "OI"

N = int(input())
M = int(input())
S = input()

find = base+pad*N

cnt = 0
i = 0
C = 0
while i < M-(N*2+1):
    for j in range(N*2+1):
        C += 1
        if S[i+j] != find[j]:
            i += j
            if j == 0:
                i+=1
            break
        else:
            pass
            #print(2, S[i+j],find[j], i, j)
    else:
        cnt += 1
        #print(1, i, j, i+j, S[i:i+j], find)
        i = i+j+1
        while S[i:i+2] == pad:
            C += 1
            #print(2, i)
            cnt += 1
            i+=2


print(cnt)
#print(C)
