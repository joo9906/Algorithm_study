from itertools import combinations, permutations


def check(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    total = set()
    for i in range(1, len(numbers) + 1):
        for comb in permutations(numbers, i):
            target = ''
            for i in comb:
                target += i
            total.add(int(target))

    for num in total:
        if num == 1 or num == 0:
            continue

        if check(num):
            answer += 1
        else:
            continue
    return answer

import time
start = time.time()
print(solution("17"))
print(solution("011"))
end = time.time()
print('걸린 시간은', end-start)