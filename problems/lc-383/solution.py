class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequencyMap = {}

        for letter in magazine:
            if letter in frequencyMap:
                frequencyMap[letter] += 1
            else:
                frequencyMap[letter] = 1

        for letter in ransomNote:
            if letter in frequencyMap:
                frequencyMap[letter] -= 1
                if frequencyMap[letter] == 0:
                    del frequencyMap[letter]
            else:
                return False
            
        return True
    
def main():
    solution = Solution()

    print(solution.canConstruct("a", "b"))     # prints False
    print(solution.canConstruct("aa", "ab"))   # prints False
    print(solution.canConstruct("aa", "aab"))  # prints True

if __name__ == '__main__':
    main()
