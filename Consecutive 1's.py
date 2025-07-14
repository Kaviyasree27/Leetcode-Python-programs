nums = [1, 1, 0, 1, 1, 1]
count = 0
max_count = 0

for i in nums:
    if i == 1:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

print("Maximum consecutive 1s:", max_count)
