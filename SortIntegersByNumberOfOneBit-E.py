arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]

result = []

for num in arr:
    n = num
    count = 0
    
    while n > 0:
        count += n % 2
        n = n // 2
    
    result.append((count, num))

result.sort()

answer = []

for item in result:
    answer.append(item[1])

print(answer)