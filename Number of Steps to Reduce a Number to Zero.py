#Brute Force / Intuitive Solution
class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
                i += 1
            elif num % 2 == 1:
                num -= 1
                i += 1
            else:
                print("Error: Something went wrong.")
        return i

# Optimized Solution based on bit manipulation
        class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return num.bit_length() - 1 + num.bit_count()
