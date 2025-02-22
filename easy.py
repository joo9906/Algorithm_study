from collections import deque

# 톱니바퀴 좀 무식하게 푼 거
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