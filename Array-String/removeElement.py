def removeElement(nums, val):
    i = 0
    n = len(nums)

    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1

    return n

print(removeElement([1, 2, 3, 4], 2))
