from dataclasses import dataclass, field
from typing import List

# 자바의 Solution.RESULT에 해당
@dataclass
class RESULT:
    cnt: int = -1
    IDs: List[int] = field(default_factory=lambda: [0] * 5)

class UserSolution:
    def init(self, N: int) -> None:
        return

    def add(self, mID: int, mGenre: int, mTotal: int) -> int:
        return -1

    def erase(self, mID: int) -> int:
        return -1

    def watch(self, uID: int, mID: int, mRating: int) -> int:
        return -1

    def suggest(self, uID: int) -> RESULT:
        res = RESULT()
        res.cnt = -1
        return res
