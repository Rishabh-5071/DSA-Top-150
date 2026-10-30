
# brute force but optimal
def majorityElement(nums):
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    max_count = -1 
    ans = -1

    for key, val in counter.items():
        if val > max_count:
            max_count = val
            ans = key

    return ans


#optimal 2 (weird logic i didnt understand)
def majorityElement2(nums):
    ans = -1
    count = 0

    for num in nums:
        if count == 0:
            ans = num

        if ans = num:
            count += 1
        else:
            count -= 1

    return ans
    #time: O(n)
    #space: O(1)






print(majorityElement([3, 2, 3]))


