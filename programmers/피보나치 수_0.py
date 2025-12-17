import sys
sys.setrecursionlimit(100001)

# 지금 이거 터짐. 고쳐야함
def solution(n):
    answer = 0

    def fibo(n):
        if n == 1:
            return 1
        elif n == 0:
            return 0
        return fibo(n - 1) + fibo(n - 2)

    target = fibo(n)
    answer = target % 1234567

    return answer