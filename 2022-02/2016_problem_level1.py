from re import search


def solution(a, b):
    
    day_num = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    day_name = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    searching_mon = day_num[0:a-1]
    
    sum_day = sum(searching_mon) + b
    
    answer = day_name[((sum_day-1) % 7)]
    
    return answer

a = 5 

b = 24 

print(solution(a,b))