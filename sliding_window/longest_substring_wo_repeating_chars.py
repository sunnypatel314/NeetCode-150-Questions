class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_seq = 0
        l = 0
        hashset = set()
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            longest_seq = max(r-l+1, longest_seq)
                    
        return longest_seq 
        
solution = Solution()

print(solution.lengthOfLongestSubstring(s = "zxyzxyz")) # 3
print(solution.lengthOfLongestSubstring(s = "xxxx")) # 1