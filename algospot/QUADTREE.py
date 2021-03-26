import sys
input = lambda : sys.stdin.readline().rstrip()

def check(board, curr):
    _curr = board[curr]
    #print(_curr, end="")
    #ret = [0, _curr]
    if _curr == "x":
        #3, 4, 1, 2
        curr, res1 = check(board,curr+1)
        curr, res2 = check(board, curr)
        curr, res3 = check(board, curr)
        curr, res4 = check(board, curr)
        return curr, _curr+res3+res4+res1+res2
    else:
        return curr+1, _curr
    

T = int(input())


for t in range(T):
    stack = [0]
    board = input()

    print(check(board, 0)[1])
    
