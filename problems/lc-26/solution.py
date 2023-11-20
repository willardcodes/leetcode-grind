from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        i, j = 1, 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
    
def main():
    solution = Solution()
    print(solution.removeDuplicates([1,1,2]))                # prints 2, nums = [1, 2, ...]
    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # prints 5, nums = [0, 1, 2, 3, 4, ...]

if __name__ == '__main__':
    main()
