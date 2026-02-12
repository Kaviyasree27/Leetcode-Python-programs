s = "abbac"
maxLen=0
for i  in range(len(s)):
    seen={}
    for j in range(i,len(s)):
        if s[j] not in seen:
             seen[s[j]]=1
        else:
            seen[s[j]]+=1
        if len(set(seen.values()))==1:
            maxLen=max(maxLen,j-i+1)
            
        
print(maxLen)
        
    