def solution(citations):
    answer = 0
    cit = sorted(citations, reverse = True)
    n = len(cit)
    for i in range(n):
        target = cit[i]
        if len(cit[i:]) >= target and target > cit[i+1]:
            return target

print(solution([3, 0, 6, 1, 5]))