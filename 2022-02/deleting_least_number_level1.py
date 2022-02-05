
def solution(arr):
    
    if len(arr) == 1:
        return [-1]
    
    del arr[arr.index(min(arr))]
    
    return arr


arr = [4,3,2,1]

print(solution(arr))


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
