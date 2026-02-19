import heapq

def solution(jobs):
    # answer는 기본값이고 now와 i의 시작점은 0이니까 일단 지정
    answer, now, i = 0, 0, 0
    start = -1
    q = []

    # 요청 시간 순으로 정렬
    jobs.sort()

    while i < len(jobs):
        for j in range(i, len(jobs)):
            # 작업의 시작 시점이 현시점 이전이라면 넣음
            if start < jobs[j][0] <= now:
                # 소요시간(dur) 기준으로 (dur, 요청시간) 넣음
                heapq.heappush(q, [jobs[j][1], jobs[j][0]])
            elif jobs[j][0] > now:
                break  # 미래 작업이 나오면 중단

        if q:
            current_dur, current_start = heapq.heappop(q)
            start = now
            now += current_dur
            # 반환 시간 = (작업 종료 시점 - 요청 시점)
            answer += (now - current_start)
            i += 1  # 처리한 작업 수 카운트
        else:
            # 지금 처리할 수 있는 작업이 없으면 다음 요청으로 이동
            now += 1

    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [3, 5]]))