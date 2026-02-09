import sys

# 입력 최적화를 위해 sys.stdin.read 사용
input = sys.stdin.readline

# 첫 번째 값은 과일의 개수 N
n = int(input().strip())

# 나머지 값들은 과일의 종류 S1, S2, ..., SN
fruits = list(map(int, input().strip().split()))

# 과일 종류별 개수를 저장할 배열 (과일 종류는 1~9번이므로 크기 10)
# 딕셔너리보다 배열 접근이 더 빠를 수 있음
fruit_counts = [0] * 10

# 현재 구간 내의 과일 종류 수
distinct_types = 0

left = 0
max_len = 0

# 슬라이딩 윈도우 (Two Pointers)
for right in range(n):
    # 오른쪽 과일 추가
    current_fruit = fruits[right]
    
    if fruit_counts[current_fruit] == 0:
        distinct_types += 1
    fruit_counts[current_fruit] += 1
    
    # 과일 종류가 2개를 초과하면 왼쪽에서 줄이기
    while distinct_types > 2:
        left_fruit = fruits[left]
        fruit_counts[left_fruit] -= 1
        
        if fruit_counts[left_fruit] == 0:
            distinct_types -= 1
        
        left += 1
        
    # 최대 길이 갱신
    # 현재 구간 길이: right - left + 1
    max_len = max(max_len, right - left + 1)
    
print(max_len)