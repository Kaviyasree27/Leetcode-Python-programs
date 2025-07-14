nums=[1,2,3,2]
y=[]
for i in nums:
    if nums.count(i)==1:
        y.append(i)
print((sum(y)))
    