from itertools import combinations

def solution(n, q, ans):
    answer = 0
    num_list = [i for i in range(1, n+1)]

    for comb in combinations(num_list, 5):
        same = []
        for check in q:
            cnt = 0
            for i in comb:
                if i in check:
                    cnt += 1

            same.append(cnt)

        if same == ans:
            answer += 1

    return answer

print(solution(15,	[[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]],	[2, 1, 3, 0, 1]))