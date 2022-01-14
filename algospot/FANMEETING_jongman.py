import sys
input = lambda : sys.stdin.readline().rstrip()

C = int(input())

for c in range(C):
    member = input().replace("F","0").replace("M", "1")
    fan = input().replace("F","0").replace("M", "1")
    member = member[::-1]

    m_l = len(member)
    f_l = len(fan)
    r_l = m_l + f_l - 1
    
    res = int(member)*int(fan)

    f_head = "{0:0"+str(f_l)+"}"
    res = f_head.format(res)[-f_l:]
    if(1-m_l != 0):
        res = res[:1-m_l]
    
    print(res.count("0"))
