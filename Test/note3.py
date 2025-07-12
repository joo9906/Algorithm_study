############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def analyze_treasures(treasure_list, threshold):
    result = {}
    for i in treasure_list:
        if i in result.keys():
            continue
        else:
            result[i] = treasure_list.count(i)
    cnt = 0
    for j in result.values():
        if int(j) > threshold:
           cnt += 1
    return result, cnt
    # 여기에 코드를 작성하여 함수를 완성합니다.


print(analyze_treasures(["gold", "silver", "gold", "diamond", "coin", "coin"], 1))
# ({'gold': 2, 'silver': 1, 'diamond': 1, 'coin': 2}, 2)

print(analyze_treasures([], 3))
# ({}, 0)

print(analyze_treasures(["pearl", "pearl", "ruby"], 2))
# ({'pearl': 2, 'ruby': 1}, 0)
#####################################################

