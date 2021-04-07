"""
Input: an-ascending-order sorted array numbers, a target number

Output: the indicies of the two numbers as an integer array of size 2

1 <= ans[0] < ans[1] <= len(nums)

condition 1: one solution
condition 2: the same element may not be used twice

"""

class Solution:
    # Two pointers
    # O(n) in time and O(1) in space
    # 36ms
    def twoSum1(self, nums, target):
        left, right = 0, len(nums) - 1

        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                left += 1
            else: right -= 1

    # hash map
    # O(n) in time and O(n) in space
    # 56 ms
    def twoSum2(self, nums, target):
        visited = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in visited:
                return [visited[n]+1, i+1]
            visited[num] = i

    # binary search
    # O(nlogn) in time and O(1) in space
    # 44ms
    def twoSum3(self, nums, target):
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            tmp = target - nums[i]
            while l <= r:
                mid = l + (r-l)//2 # // 整除 and construct a binary search tree
                if nums[mid] == tmp:
                    return [i+1, mid+1]
                elif nums[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1

    # 36 ms
    def twoSum(self, nums, target):
        visited = []
        for i in range(len(nums)):
             if nums[i] not in visited:
                 visited.append(nums[i])

                 l, r = i+1, len(nums) - 1
                 tmp = target - nums[i]
                 while l <= r:
                     mid = l + (r-l)//2 # // 整除 and construct a binary search tree
                     if nums[mid] == tmp:
                         return [i+1, mid+1]
                     elif nums[mid] < tmp:
                         l = mid + 1
                     else:
                         r = mid - 1
