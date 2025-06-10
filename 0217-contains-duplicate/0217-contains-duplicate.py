class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1
        # hashset = {}
        # for i in range(len(nums)):
        #     if nums[i] in hashset.values():
        #         return True
        #     else:
        #         hashset[i] = nums[i]
        # return False
        # 2
        # hashSet = set()
        # for i in nums:
        #     if i in hashSet:
        #         return True
        #     hashSet.add(i)
        # return False
        # 3
        # a = {}
        # for i,n in enumerate(nums):
        #     if n in a:
        #         return True
        #     a[n] = i
        # return False
        # 4
        return len(nums) != len(set(nums)) 