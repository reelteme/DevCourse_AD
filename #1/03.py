def solution(skill, skill_trees):
    d_skill = list(skill)
    d_skill.append("0")
    answer = 0
    for i in skill_trees :
        count = 0
        d_check = list(i)
        for j in d_check :
            if j in d_skill :
                if j != d_skill[count] :
                    break
                count += 1
            if j == d_check[len(i)-1] :
                answer += 1
    
    return answer