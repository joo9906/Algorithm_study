##------------------------------------ n*n 행렬 대각선 수 더하기기
# arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
# cross_sum = 0
# for i in range(5):
#     cross_sum += arr[i][i]
# for j in range(5):
#     cross_sum += arr[j][4-j]
# cross_sum -= arr[2][2]

# print(cross_sum)
# print(1+5+7+9+13+17+19+21+25)

##----------------------------------- 5*5 행렬 i,j기준 상하좌우 더해서 최댓값
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# total = 0

# for i in range(5):
#     for j in range(5):
#         for di,dj in [[0,1], [1,0], [0, -1], [-1, 0]]
#             ni = i + di
#             nj = j + dj
#             if 0<=ni<=N and 0<=nj<=N:
#                 total += abs(arr[ni][nj] - arr[i][j])

# print(total)

# ##--------------------------------------
# bit = [1, 2, 3]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for p in range(3):
#                 if bit[p]:
#                     print(bit[p], end = ' ')
#             print(bit)   

#-----------------------------------------
arr = [1,3,5]
n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (i << j):
            print(arr[j], end = ', ')
    print()
print()