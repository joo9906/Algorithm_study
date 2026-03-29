from collections import deque


def solution(n, words):
    answer = [0, 0]
    words = deque(words)
    check = set()

    turn = 1
    prev = words.popleft()
    check.add(prev)
    num = 1

    while words:  # words에 단어가 남아있거나 이전 단어와 연결되지 않으면 종료
        nxt = words.popleft()
        num += 1

        if (nxt in check) or (prev[-1] != nxt[0]):  # 끝말잇기에 실패했거나 이미 나온 단어를 말한 경우 종료
            return [num, turn]

        check.add(nxt)
        prev = nxt

        if num == n:  # 만약 인원수만큼 이어졌다면 1번 사람으로 다시 돌아감
            num = 0
            turn += 1

    return answer