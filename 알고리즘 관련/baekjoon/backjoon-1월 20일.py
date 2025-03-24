#백준 10810 - 공넣기
# n,m=map(int,input().split())
# basket=[0]*n

# for i in range(m):
#     i,j,k=list(map(int,input().split()))
#     for x in range(i,j+1):
#         basket[x-1]=k

# for x in range(n):
#     print(basket[x], end=" ")
#------------------------------
#백준 10813-공바꾸기 - 생각잘하기
# N, M= list(map(int,input().split()))
# basket=list(range(1,N+1))

# for i in range(M):
#     a, b=list(map(int,input().split()))
#     basket[a-1], basket[b-1] = basket[b-1], basket[a-1]

# print(*basket)
#-----------------------------
#백준 5597 - 과제 안 내신 분..? - remove 함수수
# student=list(range(1,31))

# for i in range(28):
#     sub=int(input())
#     student.remove(sub)

# for k in student:
#     print(k)

#-----------------
#백준 3052
# number=[]

# for i in range(10):
#     num=int(input())
#     k=num%42
#     number.append(k)

# print(len(set(number)))

#백준 10811 바구니뒤집기 - reverse 함수수
# n,m=map(int,input().split())
# bas=list(range(1,n+1))

# for k in range(m):
#     i, j=map(int,input().split())
#     bas[i-1:j]=reversed(bas[i-1:j])

# print(*bas)

# ---------------------
# 백준 1546번 - 평균
# n=int(input())
# grade=list(map(int,input().split()))
# m=max(grade)
# total_score=0

# for i in range(n):
#     score=int(grade[i])/m*100
#     total_score+=score

# print(total_score/n)
#-----------------------------------------
# 백준 27866
# s=str(input())
# i=int(input())
# print(s[i-1])
#------------------------------------
#백준 2743
# a=str(input())
# print(len(a))
#----------------------------------------
# 백준 9086 - 뭔가 좀 이상한디..
# t=int(input())

# for i in range(t):
#     lan=str(input())
#     print(lan[0]+lan[-1])
#----------------------------------------
# 백준 11654
# a=input()
# print(ord(a))
#-------------------------------------
# 백준 11720 - sum은 변수로 설정이 안된다.
# a=int(input())
# b=str(input())
# summ=0

# for i in range(a):
#     summ+=int(b[i])

# print(summ)
# ---------------------------
