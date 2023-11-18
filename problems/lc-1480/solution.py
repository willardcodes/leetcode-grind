from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        previous_sum = 0

        for i in range(len(nums)):
            previous_sum += nums[i]
            result.append(previous_sum)

        return result
    
def main():
    solution = Solution()
    print(solution.runningSum([1,2,3,4]))     # prints [1,3,6,10]
    print(solution.runningSum([1,1,1,1,1]))   # prints [1,2,3,4,5]
    print(solution.runningSum([3,1,2,10,1]))  # prints [3,4,6,16,17]


if __name__ == "__main__":
    main()