import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

class inorder():
    def __init__(self, n):
        self.n = n
        self.arr = [0] + [tuple(map(str, input().split())) for _ in range(n)]
        self.tree = [0] * (n + 2)
    
    def build(self, start, end, i = 1):
        print(start, end, i)
        if start == end:
            return self.arr[i][1]
        
        mid = (start + end) // 2
        
        if i * 2 < n:
            left = int(self.build(start, mid - 1, i * 2))
        
        op = self.arr[i][1]
        
        if i * 2 + 1 < n:
            right = int(self.build(mid + 1, end, i * 2 + 1))
    
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left // right
        
    # def calculate(self):
    #     num_stack = deque([])
    #     oper_stack = deque([])
        
    #     for chr in self.result:
    #         if chr.isdecimal():
    #             chr = int(chr)
    #             num_stack.append(chr)
    #         else:
    #             oper_stack.append(chr)
        
    #     while num_stack:
    #         if len(num_stack) == 1:
    #             return num_stack.pop()
            
    #         num1 = num_stack.popleft()
    #         op = oper_stack.popleft()
    #         num2 = num_stack.popleft()
            
    #         if op == '+':
    #             result = num1 + num2
    #             num_stack.appendleft(result)
            
    #         elif op == '-':
    #             result = num1 - num2
    #             num_stack.appendleft(result)
            
    #         elif op == '*':
    #             result = num1 * num2
    #             num_stack.appendleft(result)
            
    #         elif op == '/':
    #             result = num2 / num1
    #             num_stack.appendleft(result)
            

for i in range(1):
    n = int(input())
    tree = inorder(n)
    print(f'#{i} {tree.build(0, n-1)}')