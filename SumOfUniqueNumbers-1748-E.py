nums = [1, 2, 2, 3]
x = []
for i in range(len(nums)):
    if nums.count(nums[i]) == 1:
        x.append(nums[i])
print(sum(x))
