def solution(n):
    answer = 0
    data = [0] * (n+1)
    data[0] = -1
    data[1] = -1
    data2 = []
    for i in range(2, n+1) :
        if data[i] == 0 :
            data[i] = 1
            data2.append(i)
            if n // i > 1 :
                for j in range(1, n // i) :
                    data[i * (j+1)] = -1
                    
    if len(data2) < 3 :
        return 0
    
    print(data2)
    for i in range(len(data2)-2) :
        count = data2[i]
        for j in range(i+1, len(data2)-1) :
            count += data2[j]
            if count >= n :
                break
            for k in range(j+1, len(data2)) :
                count += data2[k]
                if count == n :
                    answer += 1
                count -= data2[k]
            count -= data2[j]
    
    
    return answer