def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    def str_to_sec(time):
        m, s = map(int, time.split(':'))
        return m * 6- + s

    def sec_to_str(time):
        m = time // 60
        s = time % 60
        return f'{m:02d}:{s:02d}'

    video_min = int(video_len[:2])
    video_sec = int(video_len[3:])
    
    now_min = int(pos[:2])
    now_sec = int(pos[3:])

    os_min = int(op_start[:2])
    os_sec = int(op_start[3:])

    oe_min = int(op_end[:2])
    oe_sec = int(op_end[3:])

    # 오프닝 중간에 낑기는 경우를 확인하기 위해
    now_total_sec = (now_min * 60) + now_sec
    os_total_sec = (os_min * 60) + os_sec
    oe_total_sec = (oe_min * 60) + oe_sec


    # 커맨드를 확인하면서 next인 경우 10초 뒤로, prev인 경우 10초 전으로
    for i in commands:
        if os_total_sec <= now_total_sec <= oe_total_sec:
            now_min, now_sec = oe_min, oe_sec

        if i == "next":
            now_sec += 10
            if now_sec >= 60:
                now_min += 1
                now_sec -= 60
                
        else:
            now_sec -= 10
            if now_sec < 0:
                if now_min == 0:
                    now_sec =0
                else:
                    now_min -= 1
                    now_sec = 60 - now_sec

    # 커맨드가 끝난 시점에서도 오프닝 사이에 낑기면 오프닝 건너뛰기 해야 함
    now_total_sec = (now_min * 60) + now_sec
    os_total_sec = (os_min * 60) + os_sec
    oe_total_sec = (oe_min * 60) + oe_sec

    if os_total_sec <= now_total_sec <= oe_total_sec:
        now_min, now_sec = oe_min, oe_sec

    
    if ((60 * video_min) + video_sec) <= ((60 * now_min) + now_sec):
        answer = video_len
        return answer

    if now_min < 10:
        now_min = f'0{now_min}'

    if now_sec < 10:
        now_sec = f'0{now_sec}'

    answer = f'{now_min}:{now_sec}'
        
    return answer

print(solution("07:22",	"04:05",	"00:15",	"04:07",	["next"]))