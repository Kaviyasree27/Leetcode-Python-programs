s = "anagram"
t="nagaram"
x= ''.join(sorted(s))
y= ''.join(sorted(t))
print(x)
print(y)
if x==y:
    print(True)
else:
    print(False)


