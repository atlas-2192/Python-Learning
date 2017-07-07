# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
# https://leetcode.com/problems/search-for-a-range/

def searchRange(nums, target):
    # if len(nums) == 0:
    #     return -1
    # elif nums[len(nums)/2] > target:
    #     return searchRange(nums[len(nums)/2:]) 
    # elif nums[len(nums)/2] < target:             
    #     return searchRange(num[:len(nums)/2]) 
    # elif nums[len(nums)/2] == target:
    #     return len(num)/2

    # return [searchRange(nums[len(nums)/2:]), searchRange(num[:len(nums)/2])]
    l_ret = lsearch(nums, target)
    print "lret"
    r_ret = rsearch(nums, target)
    return [l_ret, r_ret]

def lsearch(nums, target):
    target_index = -1
    l=0
    r=len(nums)-1
    while l <= r:
        mid = (l+r) /2
        print "L l=",l, "r=", r, " num[mid]=", nums[mid]
        if nums[mid] > target:
            l = mid - 1
            print "l=", l, " mid=", mid
        elif  nums[mid] < target:
            r = mid + 1
            print "r=", r, " mid=", mid
        else :
            target_index = mid
            r = mid - 1
            print "r=", r, " mid=", mid
    return target_index

def rsearch(nums, target):
    target_index = -1
    l=0
    r=len(nums)-1
    while l <= r:
        print "R l=",l, "r=", r
        mid = (l+r) /2
        if nums[mid] > target:
            l = mid - 1
        elif nums[mid] < target:
            r = mid + 1
        else :
            target_index = mid
            l = mid + 1
    return target_index

print searchRange([1,2,3,4], 1)