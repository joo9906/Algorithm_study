#백준 2941번
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()

# for i in croatia :
#     word = word.replace(i, '*')# input 변수와 동일한 이름의 변수
# print(len(word))
#------------------------------------------
# 1316번
# n = int(input())
# cnt = n

# for i in range(n):
#     s = list(input())
#     for c in range(0, len(s)-1):
#         if s[c] == s[c+1]:
#             pass
#         elif s[c] in s[c+1:]:
#             cnt -= 1
#             break
# print(cnt)