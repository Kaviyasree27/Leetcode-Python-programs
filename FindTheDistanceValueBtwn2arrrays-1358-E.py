arr1 = [4,5,8]
arr2 = [10,9,1,8]
d=2
count=0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if abs(arr1[i]-arr2[j])<=d:
            break
    else:
            
    
            count+=1
print(count)