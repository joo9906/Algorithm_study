def solution(targets):
    answer = 0
    targets.sort(key = lambda x: x[1])
    print(targets)
    start = 0
    end = 0

    for s, e in targets:
        if s >= end:
            start = s
            end = e
            answer += 1

    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))