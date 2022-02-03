"""
def solution(participant, completion):
    answer = ''
    for i in range(len(completion)):
        participant.remove(completion[i])

    answer = participant[0]

    return answer
"""
"""
def solution(participant, completion):
    d = dict()
    for p in participant:
        d[p] = d.get(p, 0) + 1
    for c in completion:
        d[c] -= 1
    return list(key for key, val in d.items() if val == 1).pop()
"""
#배열 array의 i번째 숫자부터 j번째 숫자까지 
# 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
#array	[1, 5, 2, 6, 3, 7, 4]
# commands[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# return	[5, 6, 3]
"""
def solution(array, commands):
    
    answer = []
    for i in range (len(commands)):
        
        n_list = array[commands[i][0]-1:commands[i][1]]
        
        new_list = sorted(n_list)
    
        answer.append(new_list[commands[i][2]-1])
        
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array,commands))
"""


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
#실패율은 다음과 같이 정의한다.
#스테이지에 도달했으나 아직 클리어하지 못한 
# 플레이어의 수 / 스테이지에 도달한 플레이어 수
#전체 스테이지의 개수 N, 
# 게임을 이용하는 사용자가 현재 멈춰있는 
# 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
# 실패율이 높은 스테이지부터 내림차순으로 
# 스테이지의 번호가 담겨있는 배열을 
# return 하도록 solution 함수를 완성하라.
"""
def solution(N, stages):
    answer = []
    answers = []
    end=[]
    total_num = int(len(stages))
    for num in range(1,N+1):
       
        answer.append(0)
        if total_num != 0:
            for i in range(len(stages)):
                if stages[i]==num:
                    answer[num-1]+=1
        
            answers.append(int(answer[num-1])/total_num)
            
            total_num -= int(answer[num-1])
        
        num+=1
    
    answers = answers[:N]    
        
    #print(answers)    
    
    answers_set = set(answers)
    
    answers_list = list(answers_set)
    
    answers_list.sort(reverse=True)

    #print(answers_list)
    
    for i in answers_list:
       
        for j in range(0,len(answers)):
            if answers[j] == i:
                end.append(j+1)
            
        
        
    return end

stages = [4,4,4,4,4,1,2,3,4,5,1]
N=6

print(solution(N,stages))
"""

#아직 미완성
#실패율


"""
def solution(num):
    answer = ''
    
    if num%2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer
"""

# 섞은 음식의 스코빌 지수 = 
# 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.

"""

def solution(scovile, K):
    num = 0
    
    scov_list = sorted(scovile)
    
    if scov_list[0] >= K:
        return -1

    else:
        while scov_list[0]< K:
            
            if len (scov_list) != 1:
                
                scov_list[0] += (2*scov_list[1])
                
                del scov_list[1]
            elif scov_list[0]< K:
                return -1
            scov_list.sort()
            
            num+=1
        
    
        return num
    
scovile = [0,0,0,0,0,0,1]

K = 7

print(solution(scovile,K))

스코빌

"""

##효율성에서 실패함.
"""
def solution(arr):
    answer = 0
    
    for i in range (len(arr)):
        answer+=arr[i]
    return answer/len(arr)

arr = [1,2,3,4]

print(solution(arr))
"""

"""
a, b= input( ).split(" ")


def star(horizontal,vertical):
    
    for i in range(0,int(vertical)):
        for j in range(0,int(horizontal)):
            print("*",end="")
        print("")
star(a,b)
"""
#별찍기
"""
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

별찍기 모범 답안
"""
"""
# 정수 X와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를
# n개 지니는 리스트를 리턴

def solution(x, n):
    answer = []
    
    for i in range(0,n):
        answer.append(x*i +x)
    return answer

x = 2
n = 5
print(solution(x,n))


#좋은 답안.
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))

return 안에 저렇게도 가능하는군...

"""

#문자열 phone_number로 주어졌을때, 전화번호의 
# 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린
# 문자열로 리턴하는 함수, solution
"""
def solution(phone_number):
    
    
    answer = list(phone_number)
    
    for i in range(0,len(phone_number)-4):
        answer[i] = "*"
    
    str_answer = ""
    
    for s in answer:
        str_answer += s
    return str_answer

phone_number = "01033334444"

print(solution(phone_number))
"""

#모범적인 답안으로는 join을 쓰지말고 return안에 문자열은 
#곱할수 있다는걸 인지하고 "*"*(len(s)-4) + s[-4:]가 나았을듯

#실패율 2트 
"""
def solution(N, stages):
    people_per = []
    #실패율 계산
    answer = []
    #실패율 순위
    people_num = []
    #각 스테이지 얼마나 있는지
    #len(people_num) = N+1 
    stages.sort()
    
    people_sum = len(stages)
    #총인원수
    for i in range(1,N+2):
        
        people_num.append(0)
        
        while len(stages) > 0:
            
            if stages[0] == i:
                
                people_num[i-1] +=1
                
                stages.pop(0)
            
            else :
                break
        
    #print(stages)
    
    #print(people_num)    
        
    for i in range(len(people_num)):
        if people_num[len(people_num)-1] == 0:
            del people_num[len(people_num)-1]
    #후반부 스테이지 클리어수 0일때 제거
    
    #print(people_num)      
    
    for i in range(len(people_num)):
        people_per.append(people_num[i]/people_sum)
        
        people_sum -= people_num[i]
    
    print(people_per)
    
    people_per = people_per[0:N]
    
    if len(people_per)< N:
        for i in range(0,N-len(people_per)):
            people_per.append(0)
            
    print(people_per)
    while max(people_per) >=0:
        for i in range(len(people_per)):
            if people_per[i] == max(people_per):
                answer.append(i+1)
                people_per[i] -=1
    
    answer = answer[:N]
    
    print(answer)
    return answer


N = 5
stages = [2,2,2,2,2,2,2,2,2,2]

solution(N,stages)
"""
"""
def solution(arr1, arr2):
    answer = []
    
    
    for i in range(len(arr1)):
        
        arr3 = []
        
        for j in range(len(arr1[0])):
            
            arr3.append(arr1[i][j] + arr2[i][j])

        answer.append(arr3)
        
    print (arr1[0])
    
    return answer

arr1 = [[1,2],[2,3]]

arr2 = [[3,4],[5,6]]

print(solution(arr1,arr2))
"""
#zip을 사용하면 더 쉽게 푸는듯.

"""
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))


"""
"""
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A


"""
#내가 할법한 케이스
#근데 이거는 A의 값을 변화시켜서 좀 그렇긴함.

# 하샤드 수
# 양의 정수 x가 하샤드 수이려면 
# x의 자릿수의 합으로 x가 나누어져야 합니다. 

#18의 자릿수 합은 1+8=9이고, 
#18은 9로 나누어 떨어지므로 18은 하샤드 수입니다
"""
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



"""
#map같은걸 쓰는 방법도 있었다


#제일 작은 수 제거하기
"""
def solution(arr):
    
    if len(arr) == 1:
        return [-1]
    
    del arr[arr.index(min(arr))]
    
    return arr


arr = [4,3,2,1]

print(solution(arr))

"""
"""
def solution(arr):
    
    if len(arr) == 1:
        return [-1]
    
    arr.sort()
    
    del arr[0]
    
    arr.reverse()
    
    return arr
    
"""
#이거 테스트케이스는 뚫리는데 정확성 테스트에선 불통함
#모든 테스트에서 이유는 우리가 sort를 써서 그런듯
# 우리가 의미 있는 난잡한 순서인데 그걸 바꿔서 그런듯

#collatz란 사람의 추측
"""
1-1. 입력된 수가 짝수라면 2로 나눕니다. 
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

"""
"""
def solution(num):
    
    answer = 0
    
    for i in range(500):
        
        if num%2 == 0:
            num /= 2
            answer += 1
        elif num == 1:
            return answer
        else:
            num = num*3 +1
            answer += 1
        
    return -1


n = 6

print(solution(n))

"""

#최대공약수와 최소공배수
#배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됨.
#3,12의 최대공약수는 3, 최소공배수는 12이므로 solution(3,12)는 [3,12]변환
"""
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
    """

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

#정수 내림차순으로 배치하기
"""
def solution(n):
    str_num = str(n)
    num_list = list(str_num)
    num_list.sort()
    num_list.reverse()
    answer_str =""
    for i in num_list:
        answer_str +=i
    
    answer_int = int(answer_str)
    
    return answer_int


n = 118372

print(solution(n))

"""

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

#수박수박수박수?
#수박 표현하기
"""
def solution(n):
    
    if n %2 == 0:
        
        return ("수박"*int(n/2))
    
    if n % 2 == 1:
        
        if n ==1:
            
            return "수"
        
        else:
            return "수" + "박수"*int(n/2) 


n = 1

print(solution(n))
"""
#내가 한것.

"""
def water_melon(n):
    s = "수박" * n
    return s[:n]
"""
#ㅈㄴ간단한 저것.

#자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태 리턴
"""
def solution(n):
    number = []
    str_num = str(n)
    
    print(str_num)
    
    list_num = list(str_num)
    
    print(list_num)
    
    reverse_num = list_num[::-1]
    
    for i in range(len(reverse_num)):
        number.append(int(reverse_num[i]))
    
    return number

n =12345


print(solution(n))
"""

#자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return
"""
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
"""

#이거 재귀함수로 풀수 있는듯?
#나중에 함 해보자

#문자열 s는 1 개 이상의 단어로 구성
#각 단어는 하나 이상의 공백문자로 구분
#각 단어의 짝수번째 알파벳은 대문자로, 
# 홀수번째 알파벳은 소문자로 문자열을 리턴하는 함수

#이상한 문자 만들기
"""

def solution(s):
    answer = ""
    num=0
    s_list = list(s)
    
    print(s_list)
    
    
    for i in range(len(s_list)):
        if s_list[i] == " ":
            answer += s_list[i]
            num=0
        else:
            if num %2 == 0:
                s_list[i] = (s_list[i].upper())
                answer += s_list[i]
                num +=1
            else :
                s_list[i] = (s_list[i].lower()) 
                answer += s_list[i]  
                num +=1
         
                
                
    return answer

s = "try hello world"

print(solution(s))


"""


#약수의 합.
"""
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i ==0:
            answer+=i
    
    
    return answer


n = 12

print(solution(n))

이거 n+answer로 return하고
조건문에 n/2이런식으로 해도

가능 
이거 좋은 이유가 만약 숫자가 크면 50000개 할걸 25000개 하게됨.
굿

"""
#서울에서 김서방 찾기
"""
def solution(seoul):
    x= seoul.index("Kim")
    
    answer = f'김서방은 {x}에 있다'
    return answer


seoul = ["Jane","Kim"]

print(solution(seoul))

"""

#문자열을 정수로 바꾸기
"""
def solution(s):
    
    s_list = list(s)
    str_num = ""
    if s_list[0] == "-":
        s_list = s_list[1:]
        for i in s_list :
            str_num += i
        answer = int(str_num)
        return -answer
    else:
        for i in s_list :
            str_num += i
        
        answer = int(str_num)
        return answer
    
    

s = "-1234"

print(solution(s))

"""
#level2 소수 찾기

#한자리 숫자가 적힌 종이 조각이 흩어져있음.
#흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려고 함.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 대, 
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return하도록 하는 solution함수

#제한 사항
#numbers의 길이는 1이상 7이하인 문자열
#numbers는 0~9까지의 숫자만으로 이루어져있음.
#"013"은 0,1,3숫자가 적힌 종이 조각이 흩어져 있다는 뜻

"""
def solution(numbers):
    num_list = list(numbers)
    
    print(num_list)
    
    
    
    answer = 0
    return answer


numbers = "17"

print(solution(numbers))

"""


#시저 암호

#각 알파벳을 일정한 거리만큼 멀어서 다른 알파벳으로 바꾸는 암호화 방식

"""

def solution(s, n):
    answer = ""
    words = list(s)
    
    print(words)
    
    for i in range(len(words)):
        if words[i] == " ":
            answer += words[i]
        elif words[i].isupper() == True:
            words[i] = chr((ord(words[i])%65+n)%26 + 65)
            answer += words[i]
        else :
            words[i] = chr((ord(words[i])%97+n)%26 + 97)
            answer += words[i]
    print(words)
    
    
    
    
    return answer


s = "a B z"

n = 4

print(solution(s,n))

"""

#아스키 코드 모르면, list에 "abdcefghijklmnopqrstuvwxyz"
#이렇게도 넣어서 가능하다.


#그리고 문자 부등호가 되는듯.. ㄷㄷ
#if i >= 'A' and i <= 'Z' 이런거...

#소수 찾기

#1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수
"""
def solution(n):
    answer = 0
    for i in range(2,n+1):
        
        num = 0
        
        for j in range(1,i+1):
            
            if num >= 3:
                
                pass
            elif i%j == 0:
                
                num +=1
        
        if num == 2:
            
            answer+=1
    
    return answer

n = 10

print(solution(n))

위에 있는건
그냥 생으로 리스트나 그런거 없이 함.

"""

#갈색은 8이상 5000이하 자연수
#노란색은 1이상 2000000이하인 자연수

#카펫의 가로 길이는 세로길이와 같거나, 세로 길이보다 김.
"""
def solution(brown, yellow):
    
    answer = []
    for i in range(3,brown//2):
        for j in range(3,i+1):
            if ((i+j-2)*2 == brown) and ((i-2)*(j-2) ==yellow):
                answer.append(i)
                answer.append(j)
                break
    
    
    return answer



brown = 24

yellow = 24

print(solution(brown,yellow))

"""
"""
def solution(brown, yellow):
    answer = []
    for i in range(3,10000):
        for j in range(3,10000):
            height = i
            width = j
            size = height * width
            k = (height - 2) * (width - 2)
            if k == yellow and size - yellow == brown:
                if width >= height:
                    answer.append(width)
                    answer.append(height)
                    return answer

"""
#위에 꺼는 태현이 꺼


#소수 찾기

#다시 해보기 

#효율성에서 실패했었음 저번껀

"""
def solution(n):
    
    num_list = []
    #전체 숫자
    none_answer = []
    #소수 아닌것들
    answer = 0
    
    for i in range(1,n+1):
        
        num_list.append(i)
        
    for i in range (4,n+1,2):
        none_answer.append(i)
    
    for i in range (6,n+1,3):
        none_answer.append(i)
    for i in range (10, n+1, 5):
        none_answer.append(i)
    
    set_num = set(num_list)
    
    set_none = set(none_answer)
    
    new_num = set_num-set_none    
        
    new_list = list(new_num)
    
    for i in new_list:
        
        num = 0
        
        for j in range(1,i+1):
            
            if num >= 3:
                
                pass
            elif i%j == 0:
                
                num +=1
        
        if num == 2:
            
            answer+=1
    
       
        
    return answer

n = 10

print(solution(n))

"""

# 효율성 실패

#이게 에라토스네스의 체 를 알아야 풀수 있음
"""
def solution(n):
    
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

        
    return len(primes)

n = 10

print(solution(n))

"""
#문자열 다루기 기본
"""
def solution(s):
    answer = True
    
    list_s=list(s)
    
    for i in list_s:
        if type(i) ==int:
            pass
        else:
            return False 
    
    return answer




s = "a234"

print(solution(s))
"""
"""
def solution(s):
    
    list_s = list(s)
    
    if len(list_s) == 4 or len(list_s) == 6 :
        pass
    else :
        return False
    
    answer = s.isdigit()
        
    return answer
"""
#isdigit()함수를 씀
#만약 문자열이 다 숫자면 True판정
#문자열 판별 - isalpha() 
#주어진 문자열이 알파벳으로만 구성되어있는지 판별하는 함수

#문자열 내 p와 y의 개수 같은지 판별하기
"""

def solution(s):
    
    p_score = 0
    y_score = 0
    s_list = list(s)
    
    for i in s_list:
        if (i == "p") or (i == "P"):
            p_score += 1
        elif (i == "y")or(i == "Y"):
            y_score += 1
            
        else:
            pass
    
    if p_score == y_score:
        return True
    
    return False


s = "oooyY"

print(solution(s))
"""

#근데 이 위에거보다 더 짧게도 가능
#upper(), lower()로 단일화를 한다음
#s.count("p")이런식으로 찾아버릴수 있다.

#두 정수 사이의 합

#두 정수 a,b가 주어졋을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수

#a와 b가 같은 경우는 둘 중 아무 수나 리턴함.
#a와 b의 대소관계는 정해져있지 않음.
"""
def solution(a, b):
    
    answer = 0
    
    max_num = max(a,b)
    
    min_num = min(a,b)
    
    if max_num == min_num:
        
        return max_num
    
    for i in range(min_num,max_num+1):
        answer +=i
    
    return answer

a=3
b=5

print(solution(a,b))
"""

#문자열 내 마음대로 정렬하기 

def solution(strings, n):
     
    f = sorted(strings,key=lambda x:x[n])
    
    return f


strings = ["abce", "abcd", "cdx"]

n = 2

#아 모르겠다








