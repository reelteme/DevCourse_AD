def solution(s):
    data = list(s)
    sum = 0
    for i in data :
        if i == '(' :
            sum += 1
        else : 
            if sum > 0 :
                sum -= 1
            else : 
                return False
    if sum == 0 :
        return True    
    return False