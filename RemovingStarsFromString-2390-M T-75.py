s = "leet**cod*e"
stack = []

for ch in s:
    if ch == '*':
        if stack:
            stack.pop()  # remove previous character
    else:
        stack.append(ch)  # add current character

result = ''.join(stack)
print(result)  # Output: "lecoe"
