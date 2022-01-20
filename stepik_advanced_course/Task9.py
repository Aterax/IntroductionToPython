nums = [int(i) for i in input().split()]

for i in range(0, len(nums) - 1, 2):
    nums.insert(i, nums.pop(i + 1))
print(*nums)
