# class Trie:
#     head = {}
#
#     def add(self, word):
#         cur = self.head
#
#         for ch in word:
#             if ch not in cur:
#                 cur[ch] = {}
#             cur = cur[ch]
#
#         cur[ch] = True # 다 끝나고 마지막 ch를 True라고 설정
#
#     def search(self, word):
#         cur = self.head
#
#         for ch in word:
#             if ch not in cur:
#                 return False
#             cur = cur[ch]
#
#         if cur[ch] == True: # 마지막 ch에서 True라면 단어가 있음
#             return True
#         else:
#             return False # 마지막 ch의 값이 True가 아니라면 해당 단어는 없는거임(더 길거나 짧음)
#
#     def remove(self, word):
#         cur = self.head
#
#         for ch in word:
#             cur = cur[ch]
#         cur[ch] = False
#
# diction = Trie()
#
# diction.add("hi")
# diction.add('hello')
# print(diction.search('hi'))
# print(diction.search('hell'))



# 세그먼트 부분

from math import ceil, log

arr = [1, 6, 2, 4, 8, 3, 7]

class segment():
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (len(arr) * 4)
        # 어떤 사람은 값을 받을 때 [0] * (2**ceil(log(len(arr), 2)+1))로 받던데 트리의 남는 공간을 최소화 하려는건가?

    def build(self, left, right, i=1):  # 왼쪽 끝, 오른쪽 끝, I
        if left == right:
            self.tree[i] = self.arr[left]
            return self.tree[i]

        mid = (left + right) // 2
        self.tree[i] = self.build(left, mid, i * 2) + self.build(mid + 1, right, i * 2 + 1)
        return self.tree[i]

    '''start = 구간의 왼쪽 end = 구간의 오른쪽, left = 찾는 범위 왼쪽, right = 찾는 범위 오른쪽
    만약 인덱스 3~5까지를 찾으려면 search(0, 6, 3, 5) 하면 될 듯

    얼추 이해는 되고 있는데 start랑 end를 그냥 0, len(arr)-1로 고정해도 되는거 아닌가?
    search에서도 그렇고 update도 그렇고 계속 고정값으로 받고 있는데?
    만약 start랑 end값을 다르게 받으면 어떤 식으로 범위가 새로 설정되는지 이해가 안됨'''

    def search(self, start, end, left, right, i=1):
        if end < left or start > right: # 찾으려는 범위가 전체 구간의 안쪽인지 확인
            return 0

        if left <= start and end <= right: # 여기가 좀 이해가 안됨. 아마 덩어리 부분 찾는거 같은데..
            return self.tree[i]

        mid = (start + end) // 2 # 해당 범위에 있는게 맞다면 반씩 가르면서 찾는 범위가 어디있나 확인
        return self.search(start, mid, left, right, i * 2) + self.search(mid + 1, end, left, right, i * 2 + 1)

    def update(self, start, end, target, diff, i=1):  # 근데 이러면 해당되는 리프노드는 안바뀌는거 아닌가??
        if target < start or target > end:  # 바꾸려는 위치가 구간의 안쪽이어야 한다(현재 구간에 해당되어야 한다)
            return
        self.tree[i] += diff  # 리프노드까지 들어가면서 차이를 다 더해줌
        if start != end:  # 리프노드가 아니라면 아래의 재귀 시작
            mid = (start + end) // 2
            # 아래 과정에서 재귀를 들어갔을 때 둘 중 하나에서 현재 함수의 첫 줄에 걸러지게 됨
            self.update(start, mid, target, diff, i * 2)  # 0~6이던 구간을 0~3으로 바꿈
            self.update(mid + 1, end, target, diff, i * 2 + 1)  # 구간을 4~6으로 바꿈


seg = segment(arr)
seg.build(0, len(arr) - 1, 1)
print(seg.search(0, 6, 2, 4), seg.tree)
seg.update(0, 6, 3, 1)  # 이거 왜 2번째 레벨까지는 바뀌는데 왜 3번째부터 안바뀌지??
print(seg.search(0, 6, 2, 4), seg.tree)

'''
B형 문제 복원 - 인기 사전 문자열
주어지는 문자열들을 가지고 인기단어 목록을 만드는 것. 최대 인기단어 배열은 5개까지 가능

주어지는 문자열의 길이 3 <= str <= 10
구해야 하는 문자열 그룹 10 <= init <= 500
최대로 주어지는 문자열 개수 10000
-> 예를 들어 1만개가 주어지고 init 값이 500 이라면 9501~10000까지 문자열로 인기단어 검색을 만드는 것

top5Keyword 함수는 mRet = [None] for _ in range(k) 로 주어지고 함수에서 바꾸면 밖에도 적용되는 것
함수의 return 값은 mRet의 길이이고 3 aaa bbb ccc 에서 3과 return값이 동일하다면 True, 이후에 mRet의 값들이 aaa bbb ccc인지 확인해서 순서와 값들이 일치하면 True

문자열의 길이가 같고 문자가 하나만 다르면 같은 그룹으로 만들 수 있음
예를 들어 aaa aab는 길이가 3이고 문자가 하나만 달라서 그룹 가능.
aaa와 aab가 그룹이고 aab와 bab가 그룹이면 aaa와 bab도 그룹이다.

그룹 내에서 대표하는 문자열은 빈도수가 가장 많은 문자열이고 빈도가 같을 경우 사전순으로 나열 됨

top5Keyword에서는 그룹의 크기가 가장 큰 단어가 앞으로 오고 크기가 같다면 사전순으로 나열 
-> 좀 헷갈림. 그룹 내의 가짓수가 많은건지 총 빈도수가 큰 애가 나오는건지


input
25 100 # 테케 개수, 점수(결과가 True면 100, False면 0)
21
100 10
200 aaa
200 bbb
200 ccc
300 3 aaa bbb ccc
200 bab
200 bbb
300 3 bab aaa ccc

100 = init(int)
- 길이가 n인 배열에 문자열들을 넣어가면서 그룹을 형성해라(문자열의 길이가 n을 넘어가면 맨 처음 들어온 값을 뺌)
- a1 a2 a3 a4 a5 b1 b2 b3 b4 b5 c1 이렇게 들어오면 a1은 배열에서 빠지고 끝에 c1이 들어감

200 = add(mKeyword)
배열에 넣을 문자열.

300 = top5Keyword(mRet)
배열에 있는 단어들 중에서 인기단어 5개를 만들어라

지금 생각해보니 add까지도 그냥 배열을 만들고 top5가 들어왔을 때 그룹을 형성하고 거기서 뽑아내면 되는 거였음.
add로 저장 할 배열을 heapq로 만들어 둠. 가중치가 가장 작은 문자열을 deque에 넣어서 최대 500개를 돌리면서 본인과 그룹인 애들을 찾음.
이 과정에서 heappop을 하면 최대한 본인이랑 비슷한 애들 위주로 먼저 돌아가기 시작할거니까 시간복잡도 하락.

같은 그룹인 애들을 다시 deque에 넣고 처음 저장된 heapq를 돌면서 본인들과 그룹인 애들을 찾아서 다시 deque에 넣고 타겟 배열도 형성.
타겟 배열에 넣을 때에는 [-1, str]로 넣어서 가중치를 설정해주고 본인이 나올때마다 가중치에서 -1을 하면 타겟 배열 내에서 가장 빈도수가
높은 애가 처음으로 오니 해당 그룹의 대표는 target[0]을 해주면 됨.
그룹을 만들고 나서 top5keyword 그룹에 빈도/그룹의 크기 기준으로 나열하고 결과값 출력하면 되는거 아닐까


'''