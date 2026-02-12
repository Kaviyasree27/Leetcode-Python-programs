nums = [2,3,1,2,4,3]
target = 7
minn=float('inf')
left=0
tot=0
for right in range(len(nums)):
    tot+=nums[right]
    while tot>=target:
        minn=min(minn,right-left+1)
        
        
        tot-=nums[left]
        left+=1
if minn==float('inf'):
    print(0)
else:
    print(minn)

    