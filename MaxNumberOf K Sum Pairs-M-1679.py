nums = [1, 2, 3, 4]
k = 5

nums.sort()

i = 0
j = len(nums) - 1
count = 0

while i < j:
    summ = nums[i] + nums[j]

    if summ == k:
        count += 1
        i += 1
        j -= 1
    elif summ > k:
        j -= 1
    else:
        i += 1

print(count)
