from collections import Counter

def solution(nums):
    answer = 0
    target = len(nums) / 2
    ans = Counter(nums)

    for k, v in ans.items():
        if answer < target:
            answer += 1
        else:
            break

    return answer

print(solution([3, 2, 2, 4]))