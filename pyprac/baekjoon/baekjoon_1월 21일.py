#백준 10809 - 알파벳 찾기
# s=str(input())
# alpha="abcdefghijklmnopqrstuvwxyz"
# lis=[]

# for i in alpha:
#     if i in s:
#         print(s.index(i), end=" ")
#     else:
#         print(-1, end=" ")
#-------------------------------------------
#백준 2675
# T=int(input())

# for i in range(T):
#     R, S=input().split()
#     R=int(R)
#     re=''
#     for k in S:
#         re+=k*R
#     print(re)
#-------------------------
#백준 
# word=list(input().split())
# print(len(word))
#------------
#백준 2908
# a, b=map(str,input().split())
# a=int(a[::-1])
# b=int(b[::-1])
# print(max(a,b))
#-------------------------------------
# 백준 5622 - for if 반복해서 쓰는거 연습하기기
# word=input()
# time=0
# code=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

# for i in range(len(word)):
#     for j in code:
#         if word[i] in j:
#             time += code.index(j) + 3

# print(time)
#---------------------------------------------
# 11718
# import sys
# while True:
#     try:
#         a=input()
#         print(a.strip())
#     except:
#         break
#----------------------------------------
#백준 3003
a,b,c,d,e,f=map(int,input().split())
if a==0:
    print(1,end=" ")
else:
    print(1-a,end=" ")

if b==0:
    print(1,end=" ")
else:
    print(1-b,end=" ")

if c==0:
    print(2,end=" ")
else:
    print(2-c,end=" ")

if d==0:
    print(2,end=" ")
else:
    print(2-d,end=" ")

if e==0:
    print(2,end=" ")
else:
    print(2-e,end=" ")

if f==0:
    print(8,end=" ")
else:
    print(8-f,end=" ")