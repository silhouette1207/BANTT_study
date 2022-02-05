#최대공약수와 최소공배수
#배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됨.
#3,12의 최대공약수는 3, 최소공배수는 12이므로 solution(3,12)는 [3,12]변환

def solution(n, m):
    
    answer = []
    min_list = []
    min_num = min(m,n)
    max_num = max(m,n)
    
    for i in range(1,min_num+1):
        
        if (min_num%i ==0) and (max_num % i ==0):
            min_list.append(i)
            
    min_list.sort()
    
    min_list.reverse()
    
    answer.append(min_list[0])
    answer.append(min_num*max_num/min_list[0])
    return answer


n = 3

m = 12

print(solution(n,m))

# 여기서 유의할점은 최소공배수는 M * N / 최대공약수 라는 점이다.

"""

def solution(n):

    if n == 1:
        return 4
    for i in range(n):
        if i * i == n:
            return (i+1)*(i+1)
        elif i * i > n:
            return -1

num = 121

print(solution(num))
"""