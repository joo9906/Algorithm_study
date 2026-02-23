def solution(n):
    answer = 0
    target = str(bin(n)).count("1")

    for i in range(n + 1, 1000001):
        nxt = str(bin(i)).count("1")
        if nxt == target:
            return i