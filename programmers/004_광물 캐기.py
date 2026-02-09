def solution(picks, minerals):
    answer = 0
    
    # 1. 캘 수 있는 광물의 최대 개수만큼만 자르기 (중요!)
    # 곡괭이가 1개인데 광물이 50개라면, 앞의 5개만 캘 수 있으므로 뒤에는 계산하면 안 됨
    total_picks = sum(picks)
    minerals = minerals[:total_picks * 5]
    
    # 2. 광물을 5개씩 묶어서 피로도 가중치 계산
    grouped_minerals = []
    for i in range(0, len(minerals), 5):
        chunk = minerals[i:i+5]
        
        # 돌 곡괭이(최악의 경우)로 캤을 때의 피로도를 기준으로 가중치 산정
        weight = 0
        for m in chunk:
            if m == 'diamond': weight += 25
            elif m == 'iron': weight += 5
            else: weight += 1
            
        # (가중치, 광물 묶음) 저장
        grouped_minerals.append([weight, chunk])
    
    # 3. 가중치가 높은(캐기 힘든) 순서대로 정렬
    # 피로도가 많이 드는 묶음을 좋은 곡괭이로 처리하기 위함
    grouped_minerals.sort(reverse=True)
    
    # 4. 정렬된 광물 묶음을 순서대로 좋은 곡괭이부터 사용하여 채굴
    for _, chunk in grouped_minerals:
        if picks[0] > 0: # 다이아 곡괭이 사용
            picks[0] -= 1
            answer += len(chunk) # 다이아 곡괭이는 뭘 캐든 피로도 1
        elif picks[1] > 0: # 철 곡괭이 사용
            picks[1] -= 1
            for m in chunk:
                if m == 'diamond': answer += 5
                else: answer += 1
        elif picks[2] > 0: # 돌 곡괭이 사용
            picks[2] -= 1
            for m in chunk:
                if m == 'diamond': answer += 25
                elif m == 'iron': answer += 5
                else: answer += 1
        else:
            break # 곡괭이 소진 (위에서 잘랐기에 여기까지 올 일은 거의 없음)
            
    return answer

# 테스트
print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))