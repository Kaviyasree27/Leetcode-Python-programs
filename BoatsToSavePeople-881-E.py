x=[1,2]
x.sort()
count=0
left=0
right=len(x)-1
limit=3
while left<=right:
    if x[left]+x[right]<=limit:
        
        left+=1
        right-=1
        
    else:
        right-=1
    count+=1
print(count)