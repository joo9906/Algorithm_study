from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people))

    while people:
        # 가장 무거운 사람을 일단 꺼냄
        heavy = people.pop()

        # 가장 가벼운 사람도 같이 탈 수 있는지 확인
        if people and heavy + people[0] <= limit:
            people.popleft()

        # 어떤 경우든 보트는 하나 필요함
        answer += 1

    return answer