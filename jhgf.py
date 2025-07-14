s = "ab#c"
def s("ab#c")
stack = []
if i == "#":
    for i in s:
        if stack:
            stack.pop()
    else:
        stack.append(i)
print(''.join(stack))
    

