#자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return

def solution(n):
    number = []
    str_num = str(n)
    
    print(str_num)
    
    list_num = list(str_num)
    
    print(list_num)
    
    reverse_num = list_num[::-1]
    
    for i in range(len(reverse_num)):
        number.append(int(reverse_num[i]))
    
    return sum(number)

n =12345


print(solution(n))

#이거 재귀함수로 풀수 있는듯 나중에 풀어보자
