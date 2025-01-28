# #백준 2941번
# # croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# # word = input()

# # for i in croatia :
# #     word = word.replace(i, '*')# input 변수와 동일한 이름의 변수
# # print(len(word))
# #------------------------------------------
# # 1316번
# # n = int(input())
# # cnt = n

# # for i in range(n):
# #     s = list(input())
# #     for c in range(0, len(s)-1):
# #         if s[c] == s[c+1]:
# #             pass
# #         elif s[c] in s[c+1:]:
# #             cnt -= 1
# #             break
# # print(cnt)
# #----------------------------------------------
# # 25206번 - 처음 풀었을 때
# score = 0
# count = 0

# for i in range(20):
#     a = list(map(str, input().split()))
#     a[1] = float(a[1])
    
#     if a[2] == 'P':
#         continue
#     elif a[2] == 'A+':
#         score += 4.5 * a[1]
#         count += a[1]
        
#     elif a[2] == 'A0' :
#         score += 4.0 * a[1]
#         count += a[1]
#     elif a[2] == 'B+':
#         score += 3.5 * a[1]
#         count += a[1]
#     elif a[2] == 'B0':
#         score += 3.0 * a[1]
#         count += a[1]
#     elif a[2] == 'C+':
#         score += 2.5 * a[1]
#         count += a[1]
#     elif a[2] == 'C0':
#         score += 2.0 * a[1]
#         count += a[1]
#     elif a[2] == 'D+':
#         score += 1.5 * a[1]
#         count += a[1]
#     elif a[2] == 'D0':
#         score += 1.0 * a[1]
#         count += a[1]
#     elif a[2] == 'F':
#         score += 0.0 * a[1]
#         count += a[1]

        
# if score != 0:
#     total = round(score/count,6)
#     print(total)
# else:
#     total = 0
#     print('0.000000')
# # ------------------------------------두 번째 풀이
# score = 0
# cnt = 0

# standard = {'A+' : 4.5, 'A0':4.0, 'B+' : 3.5, 'B0' : 3.0,
#             'C+': 2.5, 'C0': 2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

# for i in range(20):
#     a, b, c = list(map(str,input().split()))
#     b = float(b)
    
#     if c == 'P':
#         continue
#     else :
#         score += standard[c] * b
#         cnt += b

# if score != 0:
#     print(round(score/cnt,6))
# else :
#     print('0.000000')
#------------------------------------------------------
# #2738
# n, m = list(map(int,input().split()))
# emp1 = []
# emp2 = []
# final = []

# for i in range(n): #emp1을 2차열 배열로 제작
#     a = list(map(int,input().split()))
#     emp1.append(a)
    
# for i in range(n):
#     b = list(map(int,input().split()))
#     emp2.append(b)
    
# for i in range(n):
#     row = [] #새로운 리스트를 만들어서 final에 넣어줌
#     for k in range(m):
#         result = emp1[i][k] + emp2[i][k]
#         row.append(result)
#     final.append(row)

# for row in final:
#     print(*row)  #*을 붙여서 언패킹을 해줘야 출력처럼 나옴

#-------------------------------------------------------
# #2566
first = []
second = []

for i in range(9): #first를 2차열 배열로 제작
    a = list(map(int,input().split()))
    first.append(a)
    
for i in first:
    a = max(i)
    second.append(a)

m = max(second)
print(m)

for i in range(9):
    for k in range(9):
        if first[i][k] == m:
            row_a = i+1
            col_a = k+1
            print(row_a, col_a)
            break