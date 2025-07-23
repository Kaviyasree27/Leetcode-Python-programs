nums = [3,5,2,3]
nums.sort()
left=0
maxSum=0
right=len(nums)-1
while left<right:
    
    pairSum=nums[left]+nums[right]
    maxSum=max(pairSum,maxSum)
    left+=1
    right-=1
print(maxSum)