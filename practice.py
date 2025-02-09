T = int(input())

def puzzle(N, K, arr):
    correct = 0
    
    for row in arr: #가로 개수 구하기
        cnt = 0
        for a in row : # 가로 1줄 순회
            if a == 1: # 1이면 cnt에 1을 더하고 0이면 cnt가 K인지(1이 연속으로 K개 만큼 나오는지) 확인하고 맞으면 correct에 +1, 아니면 cnt 초기화
                cnt += 1
            else:
                if cnt == K:
                    correct += 1
                cnt = 0
        if cnt == K: #마지막에 나오는(row[-1]이 1인 경우에도 연속성을 판단하고 맞으면 correct에 1 추가)
            correct += 1
    
    for y in range(N): # 세로 개수 구하기
        column = []
        for x in range(N):
            column.append(arr[x][y]) #세로 한 줄을 column이란 함수에 넣어서 만듬
        cnt = 0
        for a in column : # 리스트로 한 줄을 만들었으니 다음부턴 위와 동일
            if a == 1:
                cnt += 1
            else:
                if cnt == K:
                    correct += 1
                cnt = 0
        if cnt == K:
            correct += 1
            
    return correct

for i in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    print(f'#{i} {puzzle(N, K, arr)}')