from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_s1 = len(s1)
        counter_s1 = Counter(s1)
        for i in range(0, len(s2)-length_s1+1):
            counter_s2_substr = Counter(s2[i:i+length_s1])
            if counter_s1 == counter_s2_substr:
                return True
        return False
    
solution = Solution()

print(solution.checkInclusion(s1 = "abc", s2 = "lecabee")) # True
print(solution.checkInclusion(s1 = "abc", s2 = "lecaabee")) # False