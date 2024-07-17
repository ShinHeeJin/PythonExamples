nums = [1, 2, 3, 4, 5]
for i in range(len(nums) - 1):
    partial_nums = nums[i], "new", nums[i + 1]
    if i != len(nums) - 2:
        partial_nums = partial_nums[:-1]
    print(partial_nums)
