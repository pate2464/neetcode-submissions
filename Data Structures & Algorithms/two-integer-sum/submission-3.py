class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in dic:
                if i < dic[compliment]:
                    return [i, dic[compliment]]
                else:
                    return [dic[compliment], i]
            dic[nums[i]] = i
         