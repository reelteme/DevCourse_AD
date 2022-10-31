def solution(progresses, speeds):
    answer = []
    data = [0] * len(progresses)
    for i in range(len(progresses)) :
        if (100 - progresses[i]) % speeds[i] == 0 :            
            data[i] = (100 - progresses[i]) // speeds[i] 
        else : 
            data[i] = (100 - progresses[i]) // speeds[i] + 1
    
    now = data[0]
    count = 0
    for i in data :
        if i <= now :
            count += 1
        else : 
            answer.append(count)
            now = i
            count = 1
    answer.append(count)
    
    
    return answer