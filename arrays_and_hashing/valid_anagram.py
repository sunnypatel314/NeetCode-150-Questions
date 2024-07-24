from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        return counter_s == counter_t
    
solution = Solution()

print(solution.isAnagram(s="racecar", t="carrace")) # True
print(solution.isAnagram(s="jar",t="jam")) # False



