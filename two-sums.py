from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        coords = [-1,-1]
        size = len(nums)
        pivot = 1
        index = 0

        while index < size:
            if index + pivot >= size:
                pivot = pivot + 1
                index = 0

            if pivot == size and index == 0:
                break;

            if nums[index] + nums[index + pivot] == target:
                coords[0] = index
                coords[1] = index + pivot
                break;

            index = index + 1
        
        
        return coords
    
    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
    
        coords = [-1,-1]
        size = len(nums)
        indexes = {}
        
        for i in range(size):
            indexes[nums[i]] = i
            
        for i in range(size):
            find = target - nums[i]
            
            if find in indexes and indexes[find] != i:
                coords[0] = i
                coords[1] = indexes[find]
        
        return coords
                
Solution().twoSum([2,7,11,15],9)