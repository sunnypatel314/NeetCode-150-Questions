class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1

        while r >= l:
            if s[l].isalnum() == False:
                l += 1
                continue
            if s[r].isalnum() == False:
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        return True

solution = Solution()
print(solution.isPalindrome(s = "Was it a car or a cat I saw?")) # True
print(solution.isPalindrome(s = "tab a cat")) # False