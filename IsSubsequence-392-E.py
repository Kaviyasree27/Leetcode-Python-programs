s="abcd"
t="ahbgdc"
left=0
for i in t:
    if left<len(s) and s[left] ==i:
        left+=1
print(len(s)==left)
      