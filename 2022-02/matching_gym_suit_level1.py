#체육복

# 전체 학생수 2~30  도난당한 학생의 수는 1명이상 n명 이하. 중복되는 번호 없음
# 여벌의 체육복을 가져온 학생의 수는 1명이상 n명 이하이고 중복되는 번호는 없음.
# 여벌의 체육복을 가져온 학생만 빌려주기 가능
#여벌 가져온학생도 도난당했을 가능성있 이때는 체육복 못빌려줌



"""

def solution(n, lost, reserve):
    answer = n
    
    set_lost = set(lost)
    
    set_reserve = set(reserve)
    
    dif_lost = set_lost-set_reserve 
    
    dif_reserve = set_reserve - set_lost
    
    lost_list = list(dif_lost)
    
    reserve_list = list(dif_reserve)
    
    for i in range(len(lost_list)):
        if lost_list[0] in reserve_list:
            reserve_list.remove(lost_list[0])
            lost_list.remove(lost_list[0])
            
        elif lost_list[0]-1 in reserve_list:
            
            reserve_list.remove(lost_list[0]-1)
            
            lost_list.remove(lost_list[0])
            
        elif lost_list[0]+1 in reserve_list:
            
            reserve_list.remove(lost_list[0]+1)
            
            lost_list.remove(lost_list[0])
            
        elif len(reserve_list) == 0:
            break
        
    
    if len(lost_list)>0:
        return answer - len(lost_list)
    
    return answer
"""
"""
def solution(n, lost, reserve):
    answer = n
    
    set_lost = set(lost)
    
    set_reserve = set(reserve)
    
    dif_lost = set_lost-set_reserve 
    
    dif_reserve = set_reserve - set_lost
    
    lost_list = list(dif_lost)
    
    reserve_list = list(dif_reserve)
    
    for i in lost_list:
    
        if i-1 in reserve_list:
        
            reserve_list.remove(i-1)
            
            
            
        elif i + 1 in reserve_list:
        
            reserve_list.remove(i+1)
            
        else:
        
            answer-=1
    
    return answer
n = 7
lost = [1,2,3,6]
reserve = [1,4,7]

print(solution(n,lost,reserve))
"""