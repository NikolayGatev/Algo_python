def gen01(idx, vec, nums):
    if idx >= len(vec):
        print(*vec, sep='')
        return
    for num in range(nums):
        vector[idx] = num
        gen01(idx + 1, vector, nums)

size_of_list = int(input())
nums = int(input())
vector = [0] * size_of_list

gen01(0, vector, nums)