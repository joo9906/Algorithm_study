import heapq

def solution(k, tangerine):
    answer = 0
    q = []
    kind = {i:0 for i in range(1, max(tangerine)+1)}
    for j in tangerine:
        kind[j] += 1

    for num, cnt in kind.items():
        heapq.heappush(q, (-cnt, num))

    while k > 0:
        tg_cnt, tg_num = heapq.heappop(q)
        k += tg_cnt
        answer += 1

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
