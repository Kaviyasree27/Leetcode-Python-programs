# String to be modified
s = "hello"

# String containing all vowels
vowels = 'aeiouAEIOU'

# Convert string to list for easy modification
s = list(s)

# Initialize two pointers
left, right = 0, len(s) - 1

# While pointers don't cross each other
while left < right:
    # Move left pointer to a vowel
    while left < right and s[left] not in vowels:
        left += 1
    
    # Move right pointer to a vowel
    while left < right and s[right] not in vowels:
        right -= 1
    
    # Swap vowels at left and right pointers
    s[left], s[right] = s[right], s[left]
    
    # Move both pointers inward
    left += 1
    right -= 1

# Convert list back to string and print
s = ''.join(s)
print(s)
