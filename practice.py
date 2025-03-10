# D = 현재 숫자를 두배로, 네 자리수는 1만으로 나눈 나머지로 만든다
# S = 현재 숫자에서 1을 뺌. 0이라면 9999
# L = 현재 숫자를 왼쪽으로 회전함. 1234 -> 2341
# R = 현재 숫자를 오른쪽으로 회전. 1234 -> 4123
from collections import deque
import sys, heapq
sys.stdin = open('input.txt', 'r')

T = int(input())

def D(nums):
    nums = int(nums)

    if nums * 2 > 9999:
        result = str(nums * 2 % 10000)
    else:
        result = str(nums * 2)

    if len(result) == 1:
        result = '000' + result
    elif len(result) == 2:
        result = '00' + result
    elif len(result) == 3:
        result = '0' + result

    return result

def S(nums):
    nums = int(nums)

    if nums == 0:
        result = str(9999)
    else:
        result = str(nums-1)

    return result

def L(nums):
    if len(nums) == 1:
        result = nums + '0'
    elif len(nums) == 2:
        result = nums + '00'
    elif len(nums) == 3:
        result = nums + '0'
    else:
        a = deque(list(nums))
        a.append(a.popleft())
        result = ''.join(a)

    return result

def R(nums):
    if len(nums) == 1:
        result = '000' + nums
    elif len(nums) == 2:
        result = '00' + nums
    elif len(nums) == 3:
        result = '0' + nums

    a = deque(list(nums))
    a.appendleft(a.pop())
    result = ''.join(a)

    return result

def lock(start, target):
    q = deque([(start, '')])
    if len(target) == 1:
        target = '000' + target
    elif len(target) == 2:
        target = '00' + target
    elif len(target) == 3:
        target = '0' + target

    result_list = []
    while q:
        nums, save = q.popleft()

        if nums == target:
            if save[0] == 'D':
                heapq.heappush(result_list, (1, save))
            elif save[0] == 'S':
                heapq.heappush(result_list, (2, save))
            elif save[0] == 'L':
                heapq.heappush(result_list, (3, save))
            elif save[0] == 'R':
                heapq.heappush(result_list, (4, save))
        
            if len(q) == 1000:
                break

        q.append((D(nums), save + 'D'))
        q.append((S(nums), save + 'S'))
        q.append((R(nums), save + 'R'))
        q.append((L(nums), save + 'L'))
    
    while q:
        a, b = q.popleft()
        
        if len(b) < result_list[0][1]:
            if b[0] == 'D':
                heapq.heappush(result_list, (1, b))
            elif b[0] == 'S':
                heapq.heappush(result_list, (2, b))
            elif b[0] == 'L':
                heapq.heappush(result_list, (3, b))
            elif b[0] == 'R':
                heapq.heappush(result_list, (4, b))
    
    return result_list[0][1], result_list

for k in range(1, T+1):
    start, end = map(str, input().split())
    print(f'#{k} {lock(start, end)}')