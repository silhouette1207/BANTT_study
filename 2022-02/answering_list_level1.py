#1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 
# 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 
# 배열에 담아 return 하도록 solution 함수를 작성해주세요.

"""
def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    f_score = 0
    s_score = 0
    t_score = 0
    j=0
    for i in answers:
        if first[j%5] == i :
            f_score += 1
        if second[j%8] == i :
            s_score +=1
        if third[j%10] == i:
            t_score +=1
        j+=1
    max_score=max(f_score,s_score,t_score)
    
    if max_score == f_score:
        answer.append(1)
    if max_score == s_score:
        answer.append(2)
    if max_score == t_score:
        answer.append(3)
    
        
    if len(answers)>1:
        answer = sorted(answer)
    return answer 

answers = [1,3,2,4,2]

print(solution(answers))

"""