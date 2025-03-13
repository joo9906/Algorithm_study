from collections import deque
import sys, heapq
sys.stdin = open('input.txt', 'r')

T = int(input())

def solve(price, month):
    min_price = price[3] # 최저 비용을 1년 이용권으로 설정

    worst1 = 0
    for i in month:
        worst1 += price[0] * i
    












for tc in range(1, T+ 1):
    price = [list(map(int, input().split()))]
    month = [list(map(int, input().split()))]
    solve(price, month)
    print