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

#에라토스네스의 체 라는 걸 알아야됨.