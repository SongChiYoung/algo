li = [123,14,541,5143,15,341,5431,345,1,2431]

res = []
def sort_1():
    min = 9999
    for i in range(len(li)):
        min = li[i] if min > li[i] else min 
        # True 일때 결과 if 조건문 else False 일때 결과
    res.append(min)
#문제있는 코드

def insert_sort(curr = 0):
    min = curr
    for i in range(curr, len(li)):#range(시작, 끝), 시작이 생략될 경우 0부터 시작
        min = i if li[min] > li[i] else min 
    #종료시 min 에는 가장 작은 값이 있는 위치 
    #curr 에는 시작한 위치
    li[min], li[curr] = li[curr], li[min]
    #a,b = b,a 
    #a 와 b가 서로 교체됨
    #[123,14,541,5143,15,341,5431,345,1,2431]
    #  ^curr                          ^min
    #[1,14,541,5143,15,341,5431,345,123,2431]
    #   ^curr,min
    #...  반복

#[123,14,541,5143,15,341,5431,345,1,2431]

#10 -> 5 -> 2-> 1 3번
#log 10 == 3.xxxx
#O (n * log n)
#  함수 안에서 n번 반복
#  함수를 log n 번 반복

#[(123),14,541,5143,15,341,5431,345,1,2431]
def quick_sort(li, left, right):
    if right - left <= 1:
        return 

    pivot = left
    l = left+1
    r = right
    while True:
        while True:
            if l > right:
                break
            if li[l] > li[pivot]:
                break
            else:
                l += 1
        #l은 pivot 보다 큰 수를 가르킴

        while True:
            #print(l, r)
            if r <= left+1:
                break
            if li[r] < li[pivot]:
                break
            else:
                r -= 1
        #r은 pivot 보다 작은 수를 가르킴
        if r < l:
            li[r], li[pivot] = li[pivot], li[r]
            quick_sort(li, left, r-1)
            quick_sort(li, r+1, right)
            break
        else:
            li[l], li[r] = li[r], li[l]

    #[(123),14l,541l,5143,15,341,5431,345,1r,2431r]
    #          ^l                       ^r        
    #[(123),14,1,|5143,15,341,5431,345|,541,2431]
    #[(123),14,1,5143l,15r,341r,5431r,345r,541,2431]
    #            ^l   ^r
    #[(123),14,1,15,5143,341,5431,345,541,2431]
    #            ^r   ^l
    #[15,14,1,(123),5143,341,5431,345,541,2431]

    #(1234), 1, 2, 3, 5, 6, 7  

#for i in range(len(li)):
#    insert_sort(i)

quick_sort(li, 0, len(li)-1)

print(li)

