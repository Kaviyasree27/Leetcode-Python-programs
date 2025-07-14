def singleNumber(nums):
    x = []
    y = []

    for i in nums:
        if i not in x:
            x.append(i)
        else:
            y.append(i)

    for i in x:
        if i not in y:
            return i
z=singleNumber([1,4,4,7,7,1,2])
print(z)