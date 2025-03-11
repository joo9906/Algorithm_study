T = int(input())

def check():
    n, m = map(int, input().split()) # n = 배열의 길이, m = 바꿀 횟수
    arr = list(map(int, input().split())) # 초기 상태를 입력
    hard = [list(map(int, input().split())) for _ in range(m)] # 깃발을 바꿀 때 필요한 요소들을 m줄에 걸쳐 입력받아 리스트로 저장함

    for i in range(m):
        test = arr[hard[i][1]-1:hard[i][1]+hard[i][2]-1] # 입력받은 값들을 바탕으로 어디부터 어디까지의 사람이 깃발을 바꿀건지
        for j in range(len(test)): # 깃발의 상태가 바뀌는 횟수
            try:
                if test[j] == 1: # 깃발의 상태가 1이면 0으로 교환
                    arr[j+hard[i][1]-1] = 0
                elif test[j] == 0: # 깃발의 상태가 0이면 1로 교환
                    arr[j+hard[i][1]-1] = 1
            except IndexError: #hard의 3번째 요소가 값이 커서 인덱스를 벗어나는 에러가 뜨면 그냥 무시함(arr의 값에 영향을 주지 않음)
                continue


    return print(*arr)

for k in range(1, T+1):
    print(f'#{k}', end = ' ')
    check()
