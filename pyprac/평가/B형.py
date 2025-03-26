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
예를 들어 aaa aab는 길이가 3이고 문자가 하나만 달라서  그룹이다.
그룹 가능.
aaa와 aab가 그룹이고 aab와 bab가 그룹이면 aaa와 bab도
그룹 내에서 대표하는 문자열은 빈도수가 가장 많은 문자열이고 빈도가 같을 경우 사전순으로 나열 됨

top5Keyword에서는 그룹의 크기가 가장 큰 단어가 앞으로 오고 크기가 같다면 사전순으로 나열 


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

후반부에 가면 xlemlajidc 이런 식으로 10자리 문자가 주어짐
300이 나올 경우 300 5 jfalskdfjsk askdlfjasl fasdkfljasdl dkfjddlf ajskdfjl 이런 식으로 나옴
300 다음의 숫자는 최대 5

100 = init(int)
- 길이가 n인 배열에 문자열들을 넣어가면서 그룹을 형성해라(문자열의 길이가 n을 넘어가면 맨 처음 들어온 값을 뺌)
- a1 a2 a3 a4 a5 b1 b2 b3 b4 b5 c1 이렇게 들어오면 a1은 배열에서 빠지고 끝에 c1이 들어감
100은 무조건 1번

200 = add(mKeyword)
배열에 넣을 문자열.
200은 최대 1만번 작동 가능

300 = top5Keyword(mRet)
배열에 있는 단어들 중에서 인기단어 5개를 만들어라
300은 최대 100번까지 나올 수 있음
'''

'''
지금 생각해보니 add까지도 그냥 배열을 만들고 top5가 들어왔을 때 그룹을 형성하고 거기서 뽑아내면 되는 거였음.
add로 저장 할 배열을 heapq로 만들어 둠. 가중치가 가장 작은 문자열을 deque에 넣어서 최대 500개를 돌리면서 본인과 그룹인 애들을 찾음.
이 과정에서 heappop을 하면 최대한 본인이랑 비슷한 애들 위주로 먼저 돌아가기 시작할거니까 시간복잡도 하락.

같은 그룹인 애들을 다시 deque에 넣고 처음 저장된 heapq를 돌면서 본인들과 그룹인 애들을 찾아서 다시 deque에 넣고 타겟 배열도 형성.
타겟 배열에 넣을 때에는 [-1, str]로 넣어서 가중치를 설정해주고 본인이 나올때마다 가중치에서 -1을 하면 타겟 배열 내에서 가장 빈도수가
높은 애가 처음으로 오니 해당 그룹의 대표는 target[0]을 해주면 됨.
그룹을 만들고 나서 top5keyword 그룹에 빈도/그룹의 크기 기준으로 나열하고 결과값 출력하면 되는거 아닐까

이거 터질듯 ㅋㅋ루삥뽕

'''
from typing import List
from user import init, adding, top5Keyword

INIT = 100
ADD = 200
Question = 300


def run():
    flag = True
    Q = int(input())
    for _ in range(Q):  # Q개의 action 및 인풋
        inputs = iter(input.split())
        action = int(next(inputs))
        if action == 100:
            N = int(next(inputs))  # 예시 인풋 100 50
            init(N)
        elif action == 200:
            new_word = next(inputs)  # 예시 인풋 200 abc
            adding(new_word)
        elif action == 300:  # 예시 인풋 3 aaa bbb ccc
            R_list = [None for _ in range(5)]
            user_query_answer = top5Keyword(R_list, R_list:List)
            answer = int(next(inputs))
            if answer != user_query_answer:
                flag = False  # 에러 안나게 멈추지는 않고 flag만 바꾼다.
            for __ in range(answer):
                if R_list[i] != next(inputs):
                    flag = False
        else:
            flag = False  # 입력이 이상할 때
    return flag


T, marker = list(map(int, input().split()))  # 테케수, 100점만점
for tc in range(T):
    # print(f"#{tc+1}", end="")
    print(marker if run() else 0)








# 문영은 풀이 ----------------------------------------------------------------------------------
from typing import List
from collections import deque


def init(N) -> None:
    global NUMBER
    global queue
    global dt
    NUMBER = N
    queue = deque()
    dt = {3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}}


def adding(mystr) -> None:
    if len(queue) == NUMBER:
        last_word = queue.popleft()
        if dt[len(last_word)][last_word] == 1:
            dt[len(last_word)].popitem(last_word)
        else:
            dt[len(last_word)][last_word] -= 1

    else:
        queue.append(mystr)
        if dt[len(mystr)].get(mystr, None) == None:
            dt[len(mystr)][mystr] = 1
        else:
            dt[len(mystr)][mystr] += 1


def query(List: mRet[]) -> int:
    m = []
    for leng in range(3, 11):
        if dt[leng] == {}:
            continue
        else:
            # 전체를 돌며 1차 유사한 것들을 딕셔너리로 저장
            sim = {}
            for word, count in dt[leng].items():
                stack = []
                for w, val in dt[leng].items():
                    count = 0
                    for i in range(leng):
                        if word[i] != w[i]:
                            count += 1
                    if count <= 1:
                        stack.append((w, val))
                sim[word] = stack

            # bfs를 돌면서 유사도가 같은 경우를 담는다.
            v = {}
            for word, count in dt[leng].items():
                if v.get(word, None) == None:
                    v[word] = 0
                    stack = [(word,count)]

                    # bfs
                    result = []
                    while stack:
                        s, num = stack.popleft()
                        result.append((s, num))

                        for w in sim[s]:
                            if v.get(w[0], None) == None:
                                stack.append((w[0],w[1]))
                                v[w[0]]=0

                    ##########################
                    result.sort(lambda x: (-x[1], x[0]))
                    total = 0
                    for a in result:
                        total += a[1]
                    m.append(result[0][0], total)

    m.sort(lambda x: (-x[1], x[0]))
    for i in range(min(len(m), 5)):
        mRet[i] = m[i]
    answer = min(len(m), 5)

    return answer
