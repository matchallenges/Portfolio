# nums[original] + nums[iteration]
# nums[original + 1] + nums[iteration]
# iterate while iteration is smaller than len nums -> increment original indice by one then start iteration loop

class Solution:
    def twoSum(self, nums, target):
        i = 0
        o = 0
        while o < (len(nums)):
            while i < (len(nums)):
                sum_of_indices = nums[i] + nums[o]
                if o == i:
                    break
                
                if sum_of_indices == target:
                        return ([o, i])
                    
                i += 1     
            i = 0
            o += 1
            
        

solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))