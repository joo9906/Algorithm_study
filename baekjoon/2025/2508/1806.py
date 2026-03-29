from collections import defaultdict

N, target = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
cnt[0] = 1          # P0 = 0을 미리 본 것으로
s = 0               # 현재까지 누적합 P[j]
ans = 0

for idx, x in enumerate(A, start=1):  # j = 1..N
    s += x
    add = cnt[s - target]             # 이번에 더해질 양(과거의 후보 개수)
    ans += add
    # 디버그
    print(f"j={idx}, x={x}, s={s}, s-target={s-target}, "
          f"더할개수={add}, ans={ans}, cnt={dict(cnt)}")
    cnt[s] += 1

print(ans)
