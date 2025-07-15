nums1 = [1,2,3,3]
nums2 = [2,4]
x=set(nums1)
print(x)
for i in nums2:
    if i in x:
        print(i)