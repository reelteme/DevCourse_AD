def solution(no, works):
    result = 0
    works.sort(reverse = True)
    
    if len(works) == 1 :
        if works[0] - no >= 0 :
            result = (works[0] - no) ** 2
        else :
            result = 0
    else :
        for _ in range(no) :
            if works[0] == 0 :
                break
            works[0] -= 1

            if works[0] < works[1] :
                works.sort(reverse = True)
        for i in works :
            result += i**2
    return result