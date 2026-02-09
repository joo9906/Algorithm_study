def solution(n):
    answer = 0
    nums = [i for i in range(1, n + 1)]
    start = 0
    end = n

    while start < end:
        ans = sum(nums[start:end])
        print(ans, start, end)
        if ans == n:
            answer += 1
            start += 1

        elif ans < n:
            end += 1

        elif ans > n:
            end -= 1

    print(answer)
    return answer

solution(15)

import sys

sys.setrecursionlimit()