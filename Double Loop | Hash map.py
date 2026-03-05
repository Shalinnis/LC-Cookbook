#Brute force method (O(n**2)):
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # total number of elements
        n = len(nums)                     
            # Outer loop picks the first element of the pair
            for i in range(n):
                # Inner loop picks the second element, always after i
                for j in range(i + 1, n):
                    # Check if the two selected numbers add up to the target
                    if nums[i] + nums[j] == target:
                        return [i, j]

#hash map method (O(n)):
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict: number → its index
        num_dict = {}
        # iterate with index and value
        for i, num in enumerate(nums):
            # needed partner to reach target
            complement = target - num
            # if partner seen before, return its index and current index
            if complement in num_dict:
                return [num_dict[complement], i]
            # store current number and its index
            num_dict[num] = i
