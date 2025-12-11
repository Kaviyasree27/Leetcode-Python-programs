nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSum=nums[0]
currentSum=0
for i in range(len(nums)):
    currentSum=max(nums[i],currentSum+nums[i])
    maxSum=max(maxSum,currentSum)
print(maxSum)