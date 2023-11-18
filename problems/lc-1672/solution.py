from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0

        for i in range(len(accounts)):
            customerMaximum = 0
            for j in range(len(accounts[i])):
                customerMaximum += accounts[i][j]
            maximum = max(maximum, customerMaximum)

        return maximum
    
def main():
    solution = Solution()
    print(solution.maximumWealth([[1,2,3],[3,2,1]]))          # prints 6
    print(solution.maximumWealth([[1,5],[7,3],[3,5]]))        # prints 10
    print(solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))  # prints 17

if __name__ == '__main__':
    main()
