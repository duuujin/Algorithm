def solution(plans):
    answer = []
    stack = []
    
    # 시작 시간 분단위 변환----------
    for i in range(len(plans)):
        time = plans[i][1].split(":")
        hour = int(time[0])
        minute = int(time[1])
        total_time = hour * 60 + minute
        plans[i][1] = total_time
        plans[i][2] = int(plans[i][2])
    
    # 정렬
    plans.sort(key=lambda x: x[1])
    # ---------------------------
    
    for j in range(len(plans) - 1):
        name = plans[j][0]
        start = plans[j][1]
        playtime = plans[j][2]
        
        next_time = plans[j + 1][1]
        end_time = start + playtime
        
        if end_time > next_time :
            remain_time = end_time - next_time
            stack.append([name, remain_time])
        else:
            answer.append(name)
            availa_time = next_time - end_time
            
            while stack and availa_time > 0:
                name, remain = stack.pop()
                
                if availa_time >= remain:
                    answer.append(name)
                    availa_time -= remain
                
                else:
                    remain -= availa_time 
                    stack.append([name, remain])
                    availa_time = 0
                
    answer.append(plans[-1][0])
    
    while stack :
        name, remain = stack.pop()
        answer.append(name)
    
    return answer