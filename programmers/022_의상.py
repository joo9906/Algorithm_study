from collections import defaultdict


def solution(clothes):
    cloth = defaultdict()

    for name, kind in clothes:
        cloth[kind] = cloth.get(kind, 0) + 1

    answer = 1
    for cnt in cloth.values():
        answer *= (cnt + 1)

    return answer - 1