# 시간 초과가 발생하는 경우
def dnapw():
    S, P = map(int, input().split())
    DNA = input()
    DNA_list =[]
    DNA_list.extend(DNA)
    A, C, G, T = map(int, input().split())
    cnt = 0
    test = DNA_list[:P]

    for i in range(1, S-P+2): #여기에서 매번 count로 검사하며 시간이 넘어감감
        if test.count('A') >= A and test.count('C') >= C and test.count('G') >= G and test.count('T') >= T:
            cnt += 1
        
        try:
            test.remove(DNA_list[i-1])
            test.append(DNA_list[i+P-1])
        except IndexError:
            break
    return cnt

print(dnapw())

# 개선 방법

def dnapw():
    S, P = map(int, input().split())
    DNA = input()
    DNA_list =[]
    DNA_list.extend(DNA)
    A, C, G, T = map(int, input().split())
    count_dna = {'A':0, 'C' : 0, 'G' : 0, 'T' : 0} #아예 딕셔너리로 DNA값들을 설정, 0으로 초기화화
    cnt = 0

    for i in range(P): #여기~for j 이전까지 맨 처음 배정받는 문자를 확인인
        count_dna[DNA_list[i]] += 1

    if count_dna['A'] >= A and count_dna['C'] >= C and count_dna['G'] >= G and count_dna['T'] >= T:
            cnt += 1

    for j in range(P, S): # DNA_list의 j번째 요소와 j-p번째 요소를 더하고 빼며 조건에 맞는지 확인하고 맞으면 cnt += 1
        count_dna[DNA_list[j]] += 1
        count_dna[DNA_list[j-P]] -= 1
        if count_dna['A'] >= A and count_dna['C'] >= C and count_dna['G'] >= G and count_dna['T'] >= T:
            cnt += 1

    return cnt

print(dnapw())

# ----------------------------------------------------------------------
# 백준 시크릿 코드 톱니바퀴 좀 무식하게 푼 거
saw = [None] + [deque(map(int, input())) for _ in range(4)]

roll = int(input())
turn = deque()

for i in range(roll):
    n, m = map(int, input().split())
    turn.append((n, m))

def turn_clock(num):
    saw[num].appendleft(saw[num].pop())
    
def turn_counter(num):
    saw[num].append(saw[num].popleft())

def turn_func(saw, roll, turn):
    for _ in range(roll):
        num, direct = turn.popleft()
        
        if direct == 1:
            if num == 1:
                if saw[1][2] != saw[2][6]:
                    if saw[2][2] != saw[3][6]:
                        if saw[3][2] != saw[4][6]:
                            turn_counter(4)
                        turn_clock(3)
                    turn_counter(2)
                turn_clock(1)
                
            elif num == 2:
                if saw[1][2] != saw[2][6]:
                    turn_counter(1)
                    
                if saw[2][2] != saw[3][6]:
                    if saw[3][2] != saw[4][6]:
                        turn_clock(4)
                    turn_counter(3)
                turn_clock(2)
            
            elif num == 3:
                if saw[3][2] != saw [4][6]:
                    turn_counter(4)
                
                if saw[3][6] != saw[2][2]:
                    if saw[1][2] != saw[2][6]:
                        turn_clock(1)
                    turn_counter(2)
            
            elif num == 4:
                if saw[4][6] != saw[3][2]:
                    if saw[3][6] != saw[2][2]:
                        if saw[2][6] != saw[1][2]:
                            turn_counter(1)
                        turn_clock(2)
                    turn_counter(3)
                turn_clock(4)
        
        elif direct == -1:
            if num == 1:
                if saw[1][2] != saw[2][6]:
                    if saw[2][2] != saw[3][6]:
                        if saw[3][2] != saw[4][6]:
                            turn_clock(4)
                        turn_counter(3)
                    turn_clock(2)
                turn_counter(1)
                
            elif num == 2:
                if saw[1][2] != saw[2][6]:
                    turn_clock(1)
                    
                if saw[2][2] != saw[3][6]:
                    if saw[3][2] != saw[4][6]:
                        turn_counter(4)
                    turn_clock(3)
                turn_counter(2)
            
            elif num == 3:
                if saw[3][2] != saw[4][6]:
                    turn_clock(4)
                
                if saw[3][6] != saw[2][2]:
                    if saw[1][2] != saw[2][6]:
                        turn_counter(1)
                    turn_clock(2)
                turn_counter(3)
            
            elif num == 4:
                if saw[4][6] != saw[3][2]:
                    if saw[3][6] != saw[2][2]:
                        if saw[2][6] != saw[1][2]:
                            turn_clock(1)
                        turn_counter(2)
                    turn_clock(3)
                turn_counter(4)
            
    cnt = 0
    for i in range(1, 5):
        if saw[i][0] == 1:
            if i == 1:
                cnt +=1
            elif i == 2:
                cnt +=2
            elif i == 3:
                cnt += 4
            elif i == 4:
                cnt += 8
    
    return cnt

print(turn_func(saw, roll, turn))

# -------------------------------------------------------------------
# SWEA 맨 위 문제 틀린거(백트래킹 안씀)
T = int(input())

def ballon():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    for _ in range(n):
        max_score = 0
        ind = 1
        if len(arr) > 3:
            for i in range(1, len(arr)-1):
                score = arr[i-1]*arr[i+1]
                if score > max_score:
                    max_score = score
                    ind = i
                elif score == max_score:
                    if ind > i:
                        continue
                    else:
                        ind = i
                else:
                    continue
            arr.pop(ind)
            cnt += max_score
            print(max_score)

        elif len(arr) == 3:
            if arr[0] == max(arr):
                cnt += arr[0] * arr[2]
                cnt += arr[0]
                cnt += arr[0]
                break

            elif arr[2] == max(arr):
                cnt += arr[0]*arr[2]
                cnt += arr[2]
                cnt += arr[2]
                break

            elif arr[1] == max(arr):
                score = arr[0]*arr[2]
                if arr[1]*3 > score:
                    cnt += (arr[1]*3)
                else:
                    cnt += score
                    if arr[0] > arr[1]:
                        cnt += (arr[0]*2)
                    else:
                        cnt += arr[2]*2
                break              
    return cnt

for k in range(1, T+1):
    print(f'#{k} {ballon()}')

# -----------------------------------------------------------------
# 3월 10일 벽돌깨기 문제 틀린거
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())

class brick:

    def __init__(self, arr, N, W, H):
        self.arr = arr # 바뀌지 않을 맵(first에서 처음 들어갈 때 항상 얘로 받으면서 들어감)
        self.N = N # 최대 터트릴 수 있는 횟수
        self.W = W
        self.H = H
        self.max_cnt = 0
        self.total_brick = 0 # 총 벽돌의 개수
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                    self.total_brick += 1

    def gravity(self, arr):
        for i in range(self.W):
            gh = self.H - 1
            for j in range(self.H-1, -1, -1): # 맨 아래~ 맨 위까지
                if arr[j][i] != 0:
                    arr[j][i], arr[gh][i] = arr[gh][i], arr[j][i]
                    gh -= 1
        return arr


    def bomb(self, arr, x, y, now_num, total, cnt):
        if cnt == self.N:
            if total > self.max_cnt:
                self.max_cnt = total
            return
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque([])
        bomb_block = 0

        if now_num == 1: # 구슬이 맞은 부분이 1이면 0으로 바꾸고 다음 구슬을 떨어트림
            arr[x][y] = 0
            total += 1
            cnt += 1
            self.drop(arr, cnt, total)


        elif arr[x][y] > 1: # 구슬이 맞은 부분이 1보다 크면 q에 넣어서 arr의 값들을 바꿔주는 베이스를 만들어 준다
            for dx, dy in delta: # 맨 처음 구슬과 연쇄로 터지는 블록들을 q에 넣는 부분
                for _ in range(now_num-1):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < self.H and 0 <= ny < self.W and arr[nx][ny] != 0:
                        q.append((arr[nx][ny], nx, ny)) # 터진 블록이 범위 안이고 0이 아니면 값과 좌표를 q에 넣어줌
                        bomb_block += 1
                        arr[nx][ny] = 0 # 넣은 값 부분은 arr에서 0으로 바꿈(다시 방문하면 안됨)

        while q:
            num, now_x, now_y = q.popleft()

            arr[now_x][now_y] = 0 # 뽑아온 현재 좌표를 0으로 바꿈

            bomb_block += 1

            for dx, dy in delta: # 뽑아온 블록의 값이 1보다 크면 델타를 돌면서 또 터트릴 수 있는 블록을 넣음
                for _ in range(num-1):
                    nx = now_x + dx
                    ny = now_y + dy
                    if 0 <= nx <= self.H and 0 <= ny <= self.W and arr[nx][ny] != 0:
                        q.append((arr[nx][ny], nx, ny))
                        bomb_block += 1
                        arr[nx][ny] = 0

        narr = self.gravity(arr)
        self.drop(narr, total + bomb_block, cnt + 1) # 위에서 다 터트리고 정렬 된 arr을 drop에 넣어서 맨 위부터 또 떨어트림. cnt와 bomb-block는 공유


    def drop(self, arr, total, cnt): # 구슬을 떨어뜨리는 부분
        if cnt == self.N:
            return
        top = deque([(0, i) for i in range(self.W)])
        q = deque([])

        while top: # 맨 윗줄에서 모두 다 떨어트려본다
            start_x, start_y = top.popleft() # 시작하는 row(x가 0~9까지)
            while start_x < self.H and arr[start_x][start_y] == 0: # 0이 아닌 점을 만날 때 까지
                start_x += 1
            if start_x < self.H:
                q.append((arr[start_x][start_y], start_x, start_y)) # 0이 아닌 지점을 만나면 q에 넣어서 한 줄의 시작을 알림

        while q:
            tn, x, y = q.popleft()

            self.bomb(self.arr, x, y, tn, total, cnt) # 맨 처음에는 가장 위에서 떨어트리는 경우니까 0,i (i = 0 ~ W-1)

    def result(self):
        return self.total_brick - self.max_cnt

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().strip().split())) for _ in range(H)]
    solve = brick(arr, N, W, H)
    solve.drop(arr, 0, 0)

    print(f'#{tc} {solve.result()}')