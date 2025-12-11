digits = [1,2,3]
s=""
for i in digits:
    s+=str(i)
s=str(int(s)+1)
res=[]              
for i in s:
    res.append(int(i))  
print(res)