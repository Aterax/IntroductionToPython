nums = [int(i) for i in input().split()]

count = 1
for i in range(len(nums) - 1):
    if nums[i] != nums[i + 1]:
        count += 1

print(count)


