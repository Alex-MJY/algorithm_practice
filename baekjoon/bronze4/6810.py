nums = [9,7,8,0,9,2,1,4,1,8]
for _ in range(3):
    nums.append(int(input()))

nums1 = 0
nums3 = 0
for i in range(len(nums)):
    if i % 2 == 0:
        nums1 += nums[i] * 1
    else:
        nums3 += nums[i] * 3
print(f"The 1-3-sum is {nums1 + nums3}")