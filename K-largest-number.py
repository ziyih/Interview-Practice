"""
Program to solve the k largest numbers problem

@Author: Ziyi Huang

11/30/2018
"""

def k_largest_1(k, nums):
    """
    approach 1: sorting
    @pro: concise codes
    @con: the numbers in results are not in the same order as in the original list
    """
    if k <= 0: # if k is illegal, return nothing
        return None
    if k >= len(nums): # if k is too large, return the entire list
        return nums
    sortedNums = sorted(nums, reverse = True)
    return [sortedNums[i] for i in range(0, k)]

    # or in-place sorting
    # nums.sort(reverse=True)
    # return [nums[i] for i in range(0, k)]

def k_largest_2(k, nums):
     """
     approach 2: enumerate the list, eliminate the min when a larger number is found
     @pro: maintain the original order of the numbers in the result
     @con: time would be O(mn)
     """
     if k <= 0: # if k is illegal, return nothing
         return None
     if k >= len(nums): # if k is too large, return the entire list
         return nums
     res = []
     minNum = nums[0]
     # initialize the result array and keeps track of the lowest number
     for i in range(0, k):
         res.append(nums[i])
         minNum = min(minNum, nums[i])
     # enumerate till the end
     for j in range(k, len(nums)):
         if nums[j] > minNum:
             res.remove(minNum)
             res.append(nums[j])
             # update the min
             for val in res:
                 minNum = res[0]
                 minNum = min(minNum, val)
     return res

def k_largest_3(k, nums):
    """
    approach 1: sorting, then restore the original ordering of the nubmers
    @pro: concise codes while preserve the original ordering
    @con: one more auxillary data strucutre
    """
    if k <= 0: # if k is illegal, return nothing
        return None
    if k >= len(nums): # if k is too large, return the entire list
        return nums
    sortedNums = sorted(nums, reverse = True)
    # use a list to store the original indices of the resulted numbers
    indices = []
    for i in range(0, k):
        num = sortedNums[i]
        # append the number's original position to the list
        indices.append(nums.index(num))
    indices.sort()
    return [nums[i] for i in indices]

if __name__ == "__main__":
    # test = k_largest_1(3, [5, 1, 2, 9, 1])
    # test = k_largest_1(3, [3, 1, 2, 8, 11, 5, 5])

    # test = k_largest_2(3, [5, 1, 2, 9, 1])
    # test = k_largest_2(3, [3, 1, 2, 8, 11, 5, 5])

    # test = k_largest_3(3, [5, 1, 2, 9, 1])
    # test = k_largest_3(5, [3, 1, 2, 8, 11, 5, 5])
    print test
