# 수영장(sw 역량평가)
T = int(input())

def find_min_cost(price, month):
    total_cost = [0] * 13  # 누적 최소 비용
    month = [0] + month

    for i in range(1, 13):
        if i == 1:
            total_cost[i] = min((price[0] * month[i]), price[1])
        if i == 2:
            total_cost[i] = total_cost[i - 1] + min(price[0] * month[i], price[1])
        else:# 1달권, 개월권,
            total_cost[i] = min(total_cost[i - 1] + price[1], total_cost[i-1] + (price[0] * month[i]) , total_cost[i - 3] + price[2])

    return min(total_cost[12], price[3])  # 개월, 1년권들만 사용했을 때와 비교해서 함


for tc in range(1, T + 1):
    price = list(map(int, input().split()))  # 1일권, 1달권, 3개월권, 1년권
    month = list(map(int, input().split()))  # 1~12월까지 이용 일 수
    result = find_min_cost(price, month)
    print(f'#{tc} {result}')

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
