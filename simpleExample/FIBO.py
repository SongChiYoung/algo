#n 번째 피노나치 수를 찾는 코드 
#1. 문제 분할
#1 1 2 3 5 8 ...
#M 번째 피보나치 수 = M-1번째.. + M-2번째..
#fibo(M) = ...
#2. 기저조건
#1 이나 2 번째 피보나치 수는 무조건 1
#이미 계산한 문제일 경우


#e.g. ans[1] 은 1번째 피보나치 수 

def fibo(n):
    if n == 1 or n == 2:
        return 1
    if ans[n] != 0:
        return ans[n]
    result =  fibo(n-1)+fibo(n-2)
    ans[n] = result
    return result

n = int(input())
ans = [0] * (n+1)#얘도 조금 변해야 함 (16번째 줄의 if문을 어떻게 짤지 고민해보자)
print(fibo(n))