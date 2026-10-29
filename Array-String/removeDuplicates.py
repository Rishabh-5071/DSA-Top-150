def removeDuplicates(nums):
    n = len(nums)
    j = 1

    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    return j


print(removeDuplicates([1, 1, 5, 7, 7, 8]))
