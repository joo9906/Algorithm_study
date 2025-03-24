# 10025
# n, m = map(int, input().split())
# arr = [0] * 1000001

# for _ in range(n):
#     x, y = map(int, input().split())
#     arr[y-1] = x

# def polar(arr, m):
#     window = sum(arr[:m*2+1])
#     max_ice = window

#     for i in range(m*2+1, 1000001) : # 이 부분만 보고 배낌낌
#         window = window - arr[i-(m*2+1)] + arr[i]
#         if max_ice < window:
#             max_ice = window

#     return max_ice

# print(polar(arr, m))
# ------------------------------------------------------------------------
# 2559 - 수열
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# def temp(arr, n, m):
#     window = sum(arr[:m])
#     max_temp = window

#     for i in range(1, n-m+1) :
#         window = window - arr[i-1] + arr[i+m-1]
#         if max_temp < window:
#             max_temp = window

#     return max_temp

# print(temp(arr, n, m))
# ---------------------------------------------------------------------
# 12891 DNA - a c g t를 딕셔너리로 설정해서 숫자를 더하고 빼며 해결
# def dnapw():
#     S, P = map(int, input().split())
#     DNA = input()
#     DNA_list =[]
#     DNA_list.extend(DNA)
#     A, C, G, T = map(int, input().split())
#     count_dna = {'A':0, 'C' : 0, 'G' : 0, 'T' : 0}
#     cnt = 0

#     for i in range(P):
#         count_dna[DNA_list[i]] += 1

#     if count_dna['A'] >= A and count_dna['C'] >= C and count_dna['G'] >= G and count_dna['T'] >= T:
#             cnt += 1

#     for j in range(P, S):
#         count_dna[DNA_list[j]] += 1
#         count_dna[DNA_list[j-P]] -= 1
#         if count_dna['A'] >= A and count_dna['C'] >= C and count_dna['G'] >= G and count_dna['T'] >= T:
#             cnt += 1

#     return cnt

# print(dnapw())
#---------------------------------------------------------------------
# 1018 체스판 - 시작이 W/B를 구분하고 다시 칠해야 하는 부분을 더해서 result를 최소값으로 바꾸며 해결
# n, m = map(int, input().split())
# chess = [list(input()) for _ in range(n)]

# def color(n, m, chess):
#     result = 64

#     for i in range(n-7):
#         for j in range(m-7):
#             white_color = 0 #첫 시작이 W인 경우 제대로 위치한 칸들의 개수 / 시작이 B라면 다시 칠해야 할 칸의 개수
#             black_color = 0 #첫 시작이 B인 경우 제대로 위치한 칸들의 개수 / 시작이 W라면 다시 칠해야 할 칸의 개수
#             for x in range(i, i+8):
#                 for y in range(j, j+8):
#                     if (x+y) % 2 == 0:
#                         if chess[x][y] == 'W':
#                             white_color += 1
#                         if chess[x][y] == 'B':
#                             black_color += 1

#                     else:
#                         if chess[x][y] == 'B':
#                             white_color += 1
#                         if chess[x][y] == 'W':
#                             black_color += 1
#             result = min(result, white_color, black_color)

#     return result

# print(color(n, m, chess))
#-----------------------------------------------------------------
# 1913 달팽이 - 델타를 주고 벽을 만날때까지 해당 방향으로 계속 가며 수 채우기
# N = int(input())
# M = int(input())

# snail = [[0] * N for _ in range(N)]

# def Snail(snail, N, M):
#     x, y = 0, 0
#     num = N * N
#     snail[x][y] = num
#     num -= 1

#     delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 아래, 오른쪽, 위, 왼쪽
#     target_x, target_y = 1, 1

#     while num > 0: #해당 델타로 계속 진행행
#         for i, j in delta:
#             while True:  # 방향마다 계속 반복하면서 숫자를 채움
#                 nx, ny = x + i, y + j
#                 if not (0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0):
#                     break
#                 snail[nx][ny] = num
#                 if num == M:
#                     target_x, target_y = nx + 1, ny + 1
#                 num -= 1
#                 x, y = nx, ny  # 현재 위치 갱신
#             if num == 0:
#                 break
#     return snail, target_x, target_y


# pyo, x, y = Snail(snail, N, M)


# for row in pyo:
#     print(*row)
# print(x, y)
