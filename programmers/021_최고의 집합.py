def solution(n, s):
    answer = []
    if n > s:
        return [-1]

    # a로 answer를 채우고 b를 쪼개서 각각의 값들에 더해주면 가장 비슷한 숫자들로 곱해짐
    a = s // n
    b = s % n

    answer = [a] * n

    # b를 죄다 1씩 나눠줘도 한바퀴가 끝나면 무조건 0이 됨
    i = 0
    while b > 0:
        answer[i] += 1
        i += 1
        b -= 1

    return sorted(answer)

print(solution(2, 9)) # [4, 5]
print(solution(3, 1)) # [3, 4, 4]