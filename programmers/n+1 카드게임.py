from collections import deque
from itertools import combinations

def solution(coin, cards):
    n = len(cards)
    target_num = n + 1
    hand = set(cards[:n//3])
    remain = deque(cards[n//3:])
    wait = set()
    result = 1

    # 손패 안에서 바로 n+1 조합 찾기
    def check_pair(hand_card):
        for a, b in combinations(hand_card, 2):
            if a + b == target_num:
                hand_card.remove(a)
                hand_card.remove(b)
                return True, hand_card
        return False, hand_card

    # 손패 + 임시 보관 카드(wait)에서 조합 찾기
    def check_mixed_pair(hand_card, wait_card):
        for a in hand_card:
            b = target_num - a
            if b in wait_card:
                hand_card.remove(a)
                wait_card.remove(b)
                return True, hand_card, wait_card
        return False, hand_card, wait_card

    # 보관 카드끼리만 조합 찾기
    def check_wait_pair(wait_card):
        for a, b in combinations(wait_card, 2):
            if a + b == target_num:
                wait_card.remove(a)
                wait_card.remove(b)
                return True, wait_card
        return False, wait_card

    while True:
        # 일단 뽑고 시작. 뽑을게 없으면 종료
        draw = []
        for _ in range(2):
            if remain:
                draw.append(remain.popleft())
        if not draw:
            break
        wait.update(draw)

        # 손에 있는걸로만 조합
        ok, hand = check_pair(hand)
        if ok:
            result += 1
            continue

        # 손 + 뽑은애 하나로 조합
        if coin >= 1:
            ok, hand, wait = check_mixed_pair(hand, wait)
            if ok:
                coin -= 1
                result += 1
                continue

        # 뽑은 애들로만 조합
        if coin >= 2:
            ok, wait = check_wait_pair(wait)
            if ok:
                coin -= 2
                result += 1
                continue

        # 암것도 못하면 게임 종료
        break

    return result
