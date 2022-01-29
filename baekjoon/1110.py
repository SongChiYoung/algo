N = int(input())
_N = N
i = 0
while True:
    i+=1
    a = N//10
    b = N%10
    c = a+b
    N = int(b*10) + c%10
    if _N == N:
        break
print(i)
