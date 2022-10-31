def solution(m, weights):
    data = [0] * (m+1)
    queue = []
    for i in weights :
        if i <= m :
            for j in range(0, m + 1 - i) :
                if data[j] != 0 :
                    queue.append(j)
            while queue :
                x = queue.pop()
                data[x+i] += data[x]
            data[i] += 1 
    answer = data[m]
    return answer