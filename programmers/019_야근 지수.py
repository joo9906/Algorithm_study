import heapq


def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return answer

    q = []
    for w in works:
        heapq.heappush(q, -w)

    while n > 0:
        max_work = heapq.heappop(q)
        if max_work == 0:
            break
        heapq.heappush(q, max_work + 1)
        n -= 1

    for i in q:
        answer += i ** 2

    return answer