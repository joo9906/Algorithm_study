def solution(n):
    answer = 0
    start = 1
    end = 1
    current_sum = 1

    while start <= n:
        if current_sum == n:
            answer += 1
            # 합이 n과 같으면, 다음 케이스를 찾기 위해 왼쪽을 당겨옴(오른쪽을 미는건 의미 없음)
            current_sum -= start
            start += 1

        elif current_sum < n:
            # 합이 n보다 작으면 오른쪽을 확장
            end += 1

            if end > n: break  # 범위를 벗어나면 종료
            current_sum += end

        else:
            # 합이 n보다 크면 왼쪽을 축소
            current_sum -= start
            start += 1

    return answer

print(solution(15))