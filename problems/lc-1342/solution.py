class Solution:
    def numberOfSteps(self, num: int) -> int:
        stepCounter = 0

        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            stepCounter += 1

        return stepCounter
    
def main():
    solution = Solution()
    print(solution.numberOfSteps(14))   # prints 6
    print(solution.numberOfSteps(8))    # prints 4
    print(solution.numberOfSteps(123))  # prints 12

if __name__ == '__main__':
    main()
