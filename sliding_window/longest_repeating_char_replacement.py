class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_substr = 0
        count = {}
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) > k + max(count.values()):
                count[s[l]] -= 1
                l += 1
            longest_substr = max(r - l + 1, longest_substr)
        return longest_substr
            
solution = Solution()

print(solution.characterReplacement(s = "XYYX", k = 2)) # 4
print(solution.characterReplacement(s = "AAABABB", k = 1)) # 5