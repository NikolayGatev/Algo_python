def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    mean_idx = (left + right) // 2
    while left <= right:
        if nums[mean_idx] == target:
            return mean_idx
        elif target < nums[mean_idx]:
            right = mean_idx - 1
        elif target > nums[mean_idx]:
            left = mean_idx + 1
        mean_idx = (left + right) // 2
    return -1
target = int(input())
nums = [int(x) for x in input().split()]


print(binary_search(nums, target))