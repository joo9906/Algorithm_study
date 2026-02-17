def solution(routes):
    answer = 1
    routes.sort(key = lambda x: x[1])
    check = routes[0][1]

    for i in routes:
        if i[0] <= check:
            continue
        else:
            check = i[1]
            answer += 1
    return answer
