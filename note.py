if not result_list:
    if save[0] == 'D':
        heapq.heappush(result_list, (1, save))
    elif save[0] == 'S':
        heapq.heappush(result_list, (2, save))
    elif save[0] == 'L':
        heapq.heappush(result_list, (3, save))
    elif save[0] == 'R':
        heapq.heappush(result_list, (4, save))

if len(result_list) < 10 and len(result_list[0][1]) == len(save):
    if save[0] == 'D':
        heapq.heappush(result_list, (1, save))
    elif save[0] == 'S':
        heapq.heappush(result_list, (2, save))
    elif save[0] == 'L':
        heapq.heappush(result_list, (3, save))
    elif save[0] == 'R':
        heapq.heappush(result_list, (4, save))
        
elif len(result_list) == 10:
    a = 
    return 