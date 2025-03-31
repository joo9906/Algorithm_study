# 그래프마스터 - 게임 마스터 한설이
T = int(input())

def dungeon(cnt, base): # 0, 0으로 시작할 함수
    global k # 최대 비용
    
    if not route[base]: # 갈 수 있는 노드가 없으면 함수 정지
        return

    while route[base]: # 갈 수 있으면 하나씩 빼보면서 탐색
        to, cost = route[base].pop() # base에서 갈 수 있는 노드 to와 간선의 비용 cost
        check = cnt + cost # 이전까지 왔던 비용 + cost를 더함
        
        if check > k: # check가 10보다 크면 while문을 멈추고 함수 반환
            continue
        else: # check가 10보다 작으면 해당 노드를 결과에 넣음
            result.append(to) 
            dungeon(check, to) # 다음 노드 방문


    
for j in range(1, T+1):
    m, n, k = map(int, input().split())
    route = {i:[] for i in range(m)}
    for i in range(n):
        base, to, cost = map(int, input().split())
        route[base].append([to,cost])
        
    result = [] #갈 수 있는 곳들이 있는 리스트

    dungeon(0, 0)
    print(f'#{j}', *sorted(result))

# --------------------------------------------------------------------------------------
# A형 틀린거
T = int(input())

def tree_height(n, trees, day):
    global date
    if trees.count(max(trees)) == n:
        date = day
        return
    
    stack = sorted(list(set(trees)))
    biggest = stack.pop()
    while stack:
        target = stack.pop()

        if target == biggest:
            continue
        a = trees.index(target)

        if day % 2 == 0 :
            if biggest >= target + 2:
                trees[a] += 2
                tree_height(n, trees, day + 1)
                break
            elif biggest == target + 1:
                if stack:
                    continue
                else:
                    tree_height(n, trees, day + 1)


        if day % 2 == 1:
            if biggest == target + 2:
                if target == min(trees):
                    if trees.count(target) > 1:
                        trees[a] += 1
                        tree_height(n, trees, day+1)
                        break
                    else:
                        tree_height(n, trees, day+1)
                        break
                else:
                    continue

            elif biggest >= target + 1:
                trees[a] += 1
                tree_height(n, trees, day + 1)
                break

for k in range(1, T+1):
    n = int(input())
    trees = list(map(int, input().split()))
    date = 0
    tree_height(n, trees, 1)
    print(f'#{k} {date-1}')

# -----------------------------------------------------------------------------------
# A형 While 버전
T = int(input())

def tree_height(n, trees, day):
    while trees.count(max(trees)) != n:
      stack = sorted(list(set(trees)))
      biggest = stack.pop()

      while stack:
          target = stack.pop()

          if target == biggest:
              continue
          a = trees.index(target)

          if day % 2 == 0 :
              if biggest >= target + 2:
                  trees[a] += 2
                  day+=1
                  break
              elif biggest == target + 1:
                  if stack:
                      continue
                  else:
                      day+=1


          if day % 2 == 1:
              if biggest == target + 2:
                  if target == min(trees):
                      if trees.count(target) > 1:
                          trees[a] += 1
                          day+=1
                          break
                      else:
                          day+=1
                          break
                  else:
                      continue

              elif biggest >= target + 1:
                  trees[a] += 1
                  day+=1
                  break
    return day

for k in range(1, T+1):
    n = int(input())
    trees = list(map(int, input().split()))    
    print(f'#{k} {tree_height(n, trees, 1)-1}')