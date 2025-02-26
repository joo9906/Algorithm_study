from collections import deque

def word():
    words = input().strip()
    result = []
    save = deque()
    check = 0
    

    for i in words:
        if i == ' ':
            result.extend(save)
            result.append(' ')
            save = deque()
            continue
            
        if i == '<':
            check = 1
            if save:
                result.extend(save)
                save = deque()
        
        if i == '>':
            result.append(i)
            check = 0
            continue
        
        if check == 1:
            result.append(i)
        elif check == 0:
            save.appendleft(i)
            
    if save:
        result.extend(save)
    
    return print(''.join(result))

word()