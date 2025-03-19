# visited를 설정해서 방문한 곳은 다시 방문하지 않도록 설정
# 대각선으로만 움직일 수 있으니 델타
# 시간은 상관 없음. 시작점으로 돌아가면 되는 거니까 nx ny가 시작점이면 종료하도록 설정
#


from collections import deque
import sys
sys.stdin = open("input.txt", 'r')

'''
크기가 다른 집합을 병합할 때 작은 쪽 대표자만 교체를 하면 큰 쪽의 대표자로 바로 참조가 가능하니까 
재귀로 파고들어가는것보다 효율이 낫나? 오히려 find할때마다 떨어지는건가? 


'''