def fibo(n):
    if n <= 1:
        return n

    # 공간 최적화 및 모듈러 연산
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 1234567

    return b


def solution(n):
    answer = fibo(n + 1)

    return answer

print(solution(2000))