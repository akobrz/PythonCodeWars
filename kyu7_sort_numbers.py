
def solution(nums):
    if nums:
        nums.sort()
    else:
        nums=[]
    return sorted(nums or [])

print(solution([1,2,3,10,5]))
print(solution([]))