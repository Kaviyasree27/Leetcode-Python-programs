s = "abbaca"
stack=[]
for i in s:
    if stack and stack[-1]==i:
        stack.pop()
    else:
        stack.append(i)
result = ''.join(stack)
print(result)