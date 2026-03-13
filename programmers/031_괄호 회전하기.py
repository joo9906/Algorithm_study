from collections import deque


def solution(s):
    answer = 0
    new_s = list(map(str, s))

    for _ in range(len(s)):
        q = deque(new_s)
        stack = []

        while q:
            target = q.popleft()
            if not stack:
                stack.append(target)
                continue

            if target == '[' or target == '{' or target == '(':
                stack.append(target)
            elif target == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(target)
            elif target == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(target)
            elif target == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(target)

        # 회전시키기
        nxt = new_s.pop(0)
        new_s.append(nxt)

        if not stack:
            answer += 1

        else:
            continue

    return answer