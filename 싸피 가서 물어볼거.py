T = int(input())

def bus(K, N, M, tc):
    dat = [0] * N
    cnt = 0
    coordinate =


    for i in tc: #dat에 충전기 좌표를 설정
        dat[i] += 1

    #find = dat[coordinate:coordinate + K + 1] #충전기를 찾을 범위 설정

    while coordinate <= N: #배열이 끝날 때까지 반복
        find = dat[coordinate+1:coordinate + K + 1]
        if 1 not in find: #K범위 내에 충전소가 없으면 종료
            return 0
            break

        elif coordinate+3 == N:
            return cnt
            break

        elif 1 in find: #범위 내에 충전소가 있으면 해당 좌표로 이동, 충전에 1을 더하고 다음 범위 탐색
            coordinate += find.index(1, K-1)
            cnt += 1
            continue

    return cnt

for i in range(1, T+1):
    K, N, M = map(int, input().split())
    tc = list(map(int, input().split()))
    print(f'#{i} {bus(K, N, M, tc)}')