# D = 현재 숫자를 두배로, 네 자리수는 1만으로 나눈 나머지로 만든다
# S = 현재 숫자에서 1을 뺌. 0이라면 9999
# L = 현재 숫자를 왼쪽으로 회전함. 1234 -> 2341
# R = 현재 숫자를 오른쪽으로 회전. 1234 -> 4123
from collections import deque
import sys, heapq
sys.stdin = open('input.txt', 'r')

T = int(input())

class tree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)

    def build(self, num, cnt, i = 1):
        if i > self.n:
            return

        self.tree[i] = i
        self.build(i * 2)
        self.build(i * 2 + 1)

    def check(self):
        print(self.tree)




for tc in range(1, T+1):
