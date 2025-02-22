from collections import deque

# 톱니바퀴 좀 무식하게 푼 거
saw = [None] + [deque(map(int, input())) for _ in range(4)]

roll = int(input())
turn = deque()

for i in range(roll):
    n, m = map(int, input().split())
    turn.append(deque([n, m]))

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





# 깔끔하게 정리한 거
saw = [None] + [deque(map(int, input())) for _ in range(4)]

roll = int(input())
turn = [tuple(map(int, input().split())) for _ in range(roll)]

# 시계 방향 회전
def turn_clock(num):
    saw[num].appendleft(saw[num].pop())

# 반시계 방향 회전
def turn_counter(num):
    saw[num].append(saw[num].popleft())

def turn_func():
    for num, direct in turn:
        rotate = [0] * 5  # 톱니 번호는 1부터 시작하니까 5개로 만들어서 0 남김
        rotate[num] = direct  # 해당 톱니바퀴의 회전 방향 기록

        # num번째 톱니 기준 왼쪽 확인
        for i in range(num, 1, -1):
            if saw[i][6] != saw[i - 1][2]:  # 맞닿은 톱니가 다르면 반대 방향 회전
                rotate[i - 1] = -rotate[i]  # 시계/반시계가 1, -1이니까 그 뜻
            else:
                break

        # nu번째 톱니 기준 오른쪽 확인
        for i in range(num, 4):
            if saw[i][2] != saw[i + 1][6]:
                rotate[i + 1] = -rotate[i]
            else:
                break

        for i in range(1, 5):
            if rotate[i] == 1: #시계방향 회전
                turn_clock(i)
            elif rotate[i] == -1: # 반시계방향 회전
                turn_counter(i)

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

print(turn_func())
