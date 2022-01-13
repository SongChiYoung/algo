import sys
input = lambda : sys.stdin.readline().rstrip()

C = int(input())

for c in range(C):
    member = input().replace("F","0").replace("M", "1")
    fan = input().replace("F","0").replace("M", "1")

    m_l = len(member)
    f_l = len(fan)
    r_l = f_l - m_l + 1
    
    member = int(member, 2)
    fan = int(fan, 2)

    cnt = 0
    for i in range(r_l):
        if not fan & member:
            cnt += 1
        fan = fan>>1

    print(cnt)
