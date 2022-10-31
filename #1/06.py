def solution(s):
    s = list(s)
    result = []
    num = len(s) // 2
    
    if num < 2 :
        if len(s) == 3 :
            if s[0] == s[1] == s[2] :
                answer = 2
            else :
                answer = 3
        else :
            answer = len(s)
                
    else :
        for i in range(1, num + 1) :
            result_i = 0
            data = []
            now = s[0 : i]
            count = 1
            for j in range(1, len(s)//i) :
                if now == s[j*i : (j+1)*i] :
                    count += 1
                else : 
                    data.append(count)
                    count = 1
                    now = s[j*i : (j+1)*i]

                if j == len(s)//i - 1 :
                    data.append(count)

            for j in data :
                if j == 1 :
                    result_i += i
                elif j >= 2 and j <= 9 :
                    result_i += i + 1
                elif j>= 10 and j <= 99 :
                    result_i += i + 2
                else :
                    result_i += i + 3
            result_i += len(s)%i
            result.append(result_i)

        answer = min(result)
    return answer