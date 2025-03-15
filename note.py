import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

class inorder():
    def __init__(self, n):
        self.n = n
        self.arr = [0] + [tuple(map(str, input().split())) for _ in range(n)]
        self.tree = [0] * (n + 2)
    
    def build(self, start, end, i = 1):
        if start == end:
            # self.arr[i][1]이 숫자인지 확인
            if self.arr[i][1].isdigit():
                return int(self.arr[i][1])
            else:
                raise ValueError("Invalid value in the array")
        
        mid = (start + end) // 2
        
        left = self.build(start, mid-1, i * 2)
        op = self.arr[i][1]
        right = self.build(mid + 1, end, i * 2 + 1)
        
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return left / right  # 부동소수점 나눗셈
        else:
            raise ValueError("Invalid operator")

for i in range(1, 11):
    n = int(input())
    tree = inorder(n)
    print(f'#{i} {tree.build(0, n-1)}')