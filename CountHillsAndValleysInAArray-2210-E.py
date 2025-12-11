nums = [6,6,5,5,4,1]
cleaned=[nums[0]]

for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]:
        cleaned.append(nums[i])
        
count=0      
print(nums)
for i in range(1,len(cleaned)-1):
    if cleaned[i-1]< cleaned[i] and cleaned[i]>cleaned[i+1]:
            count+=1
    elif cleaned[i-1]> cleaned[i] and cleaned[i]<cleaned[i+1]:
            count+=1
print(count)