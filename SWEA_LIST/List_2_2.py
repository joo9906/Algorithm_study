# List 2-2 사다리 문제
# def findx():
#     test = [list(map(int, input().split())) for _ in range(100)]

#     for start in range(100):
#         if test[0][start] == 1:
#             x, y = start, 0

#             while y < 99:
#                 if x < 99 and test[y][x+1] == 1:
#                     while x < 99 and test[y][x+1] == 1:
#                         x += 1
#                 elif x > 0 and test[y][x-1] == 1:
#                     while x > 0 and test[y][x-1] == 1:
#                         x -= 1
#                 y += 1

#             if test[y][x] == 2:
#                 return start


# for _ in range(10):
#     T = int(input())
#     print(f'#{T} {findx()}')
# ------------------------====------------------------------------------
# List 2-2 달팽이숫자