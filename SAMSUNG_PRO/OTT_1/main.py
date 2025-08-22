# Python 3
# 자바 하니스(Solution.run/main)와 동일한 동작을 하는 파이썬 테스트 러너
# - 입력 포맷, 채점 로직, 출력 형식("#<tc> <score>")을 그대로 유지
# - UserSolution 클래스 내부만 문제 요구에 맞게 구현하면 됩니다.

import sys
from dataclasses import dataclass, field
from typing import List
from function import UserSolution

# ===== 커맨드 상수 (자바와 동일) =====
CMD_INIT    = 100
CMD_ADD     = 200
CMD_ERASE   = 300
CMD_WATCH   = 400
CMD_SUGGEST = 500

usersolution = UserSolution()

# ====== 빠른 입력 토크나이저 ======
data = sys.stdin.buffer.read().split()
it = iter(data)
def nextint() -> int:
    return int(next(it))

def run() -> bool:
    Q = nextint()
    okay = False  # 자바와 동일: INIT가 호출되면 True로 전환, 이후 오답이 있으면 False로 변경

    for _ in range(Q):
        cmd = nextint()

        if cmd == CMD_INIT:
            N = nextint()
            usersolution.init(N)
            okay = True

        elif cmd == CMD_ADD:
            mID = nextint()
            mGenre = nextint()
            mTotal = nextint()
            ret = usersolution.add(mID, mGenre, mTotal)
            ans = nextint()
            if ret != ans:
                okay = False

        elif cmd == CMD_ERASE:
            mID = nextint()
            ret = usersolution.erase(mID)
            ans = nextint()
            if ret != ans:
                okay = False

        elif cmd == CMD_WATCH:
            uID = nextint()
            mID = nextint()
            mRating = nextint()
            ret = usersolution.watch(uID, mID, mRating)
            ans = nextint()
            if ret != ans:
                okay = False

        elif cmd == CMD_SUGGEST:
            uID = nextint()
            res = usersolution.suggest(uID)
            cnt = nextint()
            if res.cnt != cnt:
                okay = False
            # 기대 정답과 res.IDs[0..cnt-1] 비교
            for i in range(cnt):
                ans = nextint()
                if i >= len(res.IDs) or res.IDs[i] != ans:
                    okay = False
        else:
            # 알 수 없는 커맨드 → 실패
            okay = False

    return okay

def main():
    TC = nextint()
    MARK = nextint()
    for tc in range(1, TC + 1):
        score = MARK if run() else 0
        # 자바와 동일한 출력 형식
        print(f"#{tc} {score}")

if __name__ == "__main__":
    main()
