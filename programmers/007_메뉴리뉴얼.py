import heapq
from copy import deepcopy
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    
    for cour in course:
        count_list = Counter()
        
        # orders를 순회하며 해당 order로 만들 수 있는 모든 조합을 count_list에 저장. count_list 내부적으로 카운트 할거임
        for order in orders:
            order = sorted(order)
            record = combinations(order, cour)
            count_list.update(record)

        max_count = max(count_list.values())
        print(count_list)
        
        # 조건 중에 2번 이상 주문했어야 한다고 함
        if max_count >= 2:
            for name, cnt in count_list.items():
                # 제일 많이 나온 조합이 맞으면 answer에 저장
                if cnt == max_count:
                    answer.append(''.join(name))
    
    # 오름차순으로 적으랫음
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))




# 기존 코드
# import heapq
# from copy import deepcopy

# def solution(orders, course):
#     answer = []
#     food = [chr(i) for i in range(65, 91)]
#     q = []
    
#     for order in orders:
#         for menu in order:
#             food[menu] += 1
    
#     for key, val in food.items():
#         if val != 0:
#             q.append((val, key))
    
#     q.sort()
    
#     for i in course:
#         result = ''
#         for_pop = deepcopy(q)
#         for _ in range(i):
#             _, name = for_pop.pop()
#             result += name
        
#         answer.append(''.join(sorted(result)))
            
        
#     return answer