import sys
input = lambda : sys.stdin.readline().rstrip()

C = int(input())

for c in range(C):
    member = input().replace("F","0").replace("M", "1")
    fan = input().replace("F","0").replace("M", "1")
    fan = fan[::-1]

    m_l = len(member)
    f_l = len(fan)
    r_l = m_l + f_l - 1
    
    res = int(member)*int(fan)

    f_head = "{0:0"+str(r_l)+"}"
    res = f_head.format(res)
    res = res[-f_l:-m_l+1]

    print(res.count("0"))

