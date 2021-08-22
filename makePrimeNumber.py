nums =[1,2,7,6,4]

def solution(nums):
    sum = 0
    count = 0
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if(primeNumber(sum)):
                    count += 1
    return count

#소수는 1과 자기자신을 제외하고 나누어지지 않는 수
def primeNumber(n):
    for i in range(2, n):
        if(n%i == 0):   #n을 1과 자기자신을 제외한 어떤 수로 나누었을때 0이라면 나누어진것으로 소수가 아님.
            return False
    return True

print(solution(nums))