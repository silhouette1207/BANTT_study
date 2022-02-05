def solution(x):
    answer = True
    
    x_str=str(x)
    x_list = list(x_str)
    x_sum = 0
    for a in x_list:
        x_sum += int(a)
        
    if x %x_sum !=0:
        return False    
    
    return answer


arr = 247
solution(arr)