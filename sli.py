x=[1,2,3,4,5,6,7,8]
k=3
result=[]
for i in range(len(x)-k+1):
    window=x[i:i+k]
    y=min(window)
    result.append(y)
print(result)
    