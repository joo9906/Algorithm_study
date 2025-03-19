# 6개의 원소 (1~6)이 존재하는 경우
N = 6
# 1~n개의 원소가 있다고 가정. 총 n개의 집합을 생성하는 함수. 각 원소의 부모(대표자는 아직 아님)를 자신으로 설정
def make_set(x): # 해당 노드의 부모 정보를 가지고 있다는 부분.
    parents = [i for i in range(x+1)]
    return parents

def find_set(x): # 부모를 찾는 함수
    # 파다보니 자신과 부모가 같다 = 대표자다
    if parents[x] == x:
        return x

    # x의 부모 노드를 기준으로 다시 대표자를 검색
    return find_set(parents[x])


# 1. x와 y가 속한 집단의 대표자 검색
# 2. 대표자들끼리 병합
def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면? 병합하면 안됨.
    if ref_x == ref_y:
        return

    # 다른 집합이라면 합친다
    # -> 문제에 따라 우선되는 집합으로 합친다.
    # -> 이번에는 더 작은 노드로 합친다
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

parents = make_set(N)
print(parents)

union(1, 3)
union(2, 3)
union(5, 6)

print(parents)

if find_set(3) == find_set(5):
    print('같음')
else:
    print('다름')


# 유니온 파인드의 경로 압축 - find 부분에서 설정
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])

    return parents[x]

# 유니온 파인드의 랭크 부분 - 생성과 병합에서 조작이 들어감
def make_set(n):
    parents = [i for i in range(n + 1)]
    ranks = [0] * (n + 1)
    return parents, ranks

#  병합 부분
def Union(x, y):
    global ranks
    
    ref_x = find_set(x)
    ref_y = find_set(y)
    
    # 더 큰 랭크를 기준으로 병합
    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:
        parents[ref_y] = ref_x  # 크기가 같으면 그냥 아무거나의 대표자로 병합함
        ranks[ref_x] += 1