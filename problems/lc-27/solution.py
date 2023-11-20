# problem link: https://leetcode.com/problems/remove-element
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        print(f"output: {j}, nums: {nums}")
        return j
    
def main():
    solution = Solution()
    solution.removeElement([3,2,2,3], 3)
    solution.removeElement([0,1,2,2,3,0,4,2], 2)

if __name__ == '__main__':
    main()
