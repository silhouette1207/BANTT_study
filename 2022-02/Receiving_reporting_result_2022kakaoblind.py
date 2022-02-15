def solution(id_list, report, k):
    id_dict = {
        
    }
    answer={
        
    }
    for i in id_list:
        id_dict[i]=0
        answer[i]=0
    print(id_dict)
    
    non_dup = []
    
    reporting_list = []
    
    for i in report:
        if i not in non_dup:
            non_dup.append(i)
    
    for i in range(len(non_dup)):
        non_dup[i]=non_dup[i].split(" ")
    
        id_dict[non_dup[i][1]] += 1
    
    for key in id_dict:
        if id_dict[key] >= k :
            reporting_list.append(key)
    print(reporting_list)
            
    print(id_dict)
    
    for i in range(len(non_dup)):
        if non_dup[i][1] in reporting_list:
            answer[non_dup[i][0]] += 1

    return list(answer.values())
id_list = ["muzi","frodo","apeach","neo"]

report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

k = 2

print(solution(id_list,report,k))