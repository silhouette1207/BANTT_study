def solution(absolutes, signs):
    
    answer = sum(absolutes)
    
    for i in range(len(signs)):
        if signs[i] == False:
            answer -= absolutes[i] *2
    
    return answer

absolutes = [4,7,12]

signs = [True,False,True]

print(solution(absolutes,signs))