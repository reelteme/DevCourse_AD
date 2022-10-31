def solution(monster, S1, S2, S3):
    answer = 0
    safe = 0
    
    
    for i in range(S1) :
        count = i+2
        for j in range(S2) :
            count += j+1
            for k in range(S3) :
                count += k+1
                if count not in monster :
                    safe += 1
                count -= (k+1)
            count -= (j+1)
    
    answer = int(safe / (S1 * S2 * S3) * 1000)
    
    return answer