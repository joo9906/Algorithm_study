# #리스트 2-1 스도쿠 문제
# # 얕은 복사를 이용해 중복되는 값이 있다면 사라지지 않아 0을 반환하게끔 함
# def sudoku(testcase):
#     answer = 1
#     compare = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
#     # 가로 줄 비교
#     for i in testcase: # 1. tc의 리스트를 가져와 i에 할당
#         if sorted(i) != compare:
#             answer = 0
#             break
    
#     #세로 줄 비교
#     for y in range(9):
#         col_list = [testcase[x][y] for x in range(9)] # testcase의 y번째 리스트의 x번째 값들을 빈 리스트에 넣음
#         if sorted(col_list) != compare:
#             answer = 0
#             break
    
#     # 3*3 비교

#     for y in range(0, 9, 3): 
#         for x in range(0, 9, 3):
#             box_list = []
#             for i in range(3):
#                 for j in range(3):
#                     box_list.append(testcase[x+i][y+j]) #x+i번째, y+i번째 값들(9개)을 box_list에 삽입
#             if sorted(box_list) != compare:
#                 answer = 0
#                 break

#     return answer

# for i in range(1, T+1):
#     testcase = []
#     for _ in range(9):
#         line = list(map(int, input().split()))
#         testcase.append(line)
#     print(f'#{i} {sudoku(testcase)}')
# 
#----------------------------------------------------------------------------------
# 리스트 2-1 낱말 문제
# T = int(input())

# def puzzle(N, K, arr):
#     correct = 0
    
#     for row in arr: #가로 개수 구하기
#         cnt = 0
#         for a in row : # 가로 1줄 순회
#             if a == 1: # 1이면 cnt에 1을 더하고 0이면 cnt가 K인지(1이 연속으로 K개 만큼 나오는지) 확인하고 맞으면 correct에 +1, 아니면 cnt 초기화
#                 cnt += 1
#             else:
#                 if cnt == K:
#                     correct += 1
#                 cnt = 0
#         if cnt == K: #마지막에 나오는(row[-1]이 1인 경우에도 연속성을 판단하고 맞으면 correct에 1 추가)
#             correct += 1
    
#     for y in range(N): # 세로 개수 구하기
#         column = []
#         for x in range(N):
#             column.append(arr[x][y]) #세로 한 줄을 column이란 함수에 넣어서 만듬
#         cnt = 0
#         for a in column : # 리스트로 한 줄을 만들었으니 다음부턴 위와 동일
#             if a == 1:
#                 cnt += 1
#             else:
#                 if cnt == K:
#                     correct += 1
#                 cnt = 0
#         if cnt == K:
#             correct += 1
            
#     return correct

# for i in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
    
#     print(f'#{i} {puzzle(N, K, arr)}')
# ------------------------------------------------------------------------
# List 2 - 1 Sum
# 
# def find_max(arr):
#     compare_list = []

#     for i in range(100):
#         compare_list.append(sum(arr[i]))

#     for i in range(100):
#         col_sum = 0
#         for j in range(100):
#             col_sum += arr[j][i]
#         compare_list.append(col_sum)

#     cross_sum = 0
#     for x in range(100):
#         cross_sum += arr[x][x]
#     compare_list.append(cross_sum)

#     rcross_sum = 0
#     for x in range(100):
#         rcross_sum += arr[x][99-x]
#     compare_list.append(rcross_sum)

#     return max(compare_list)

# for i in range(10):
#     T = int(input())
#     arr = []
#     for k in range(100):
#         num = list(map(int, input().split()))
#         arr.append(num)
#     print(f'#{T} {find_max(arr)}')
--------------------------------------------------------------------------------
# 리스트 2 - 1 파리퇴치

# T = int(input())

# def CatchFly(N, M, arr):
#     catch_fly = []
#     for i in range(M):
#         for j in range(M):
#             catch_fly.append([i, j])

#     num_catch = []

#     for x in range(N-M+1):
#         for y in range(N-M+1):
#             sum_fly = 0
#             for i, j in catch_fly:
#                 nx = x + i
#                 ny = y + j
#                 if 0 <= nx < N and 0 <= ny < N:
#                     sum_fly += arr[nx][ny]
#             num_catch.append(sum_fly)
#     result = max(num_catch)

#     return result

# for i in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     print(f'#{i} {CatchFly(N, M, arr)}')