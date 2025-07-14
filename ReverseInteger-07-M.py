
#if res > 2**31 - 1: 
            #return 0 #given in question adhu podla

def revInt(x):
    rev=""
    for i in str(abs(x)):
        rev=i+rev
    res=int(rev)
    
    if x<0:
        return -res
    else:
        return res
        
        
y=revInt(12)
z=revInt(-34)
print(y)
print(z)