words = ["cd","ac","dc","ca","zz"]
for i in range(len(words)):
    words[i] = ''.join(sorted(words[i]))
print(words)

count = 0
x = []

for i in words:
    if i not in x:
        x.append(i) 
    else:
       count=count+1
print(x)
print(count)