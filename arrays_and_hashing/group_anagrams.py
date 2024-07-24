from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            mapping[tuple(count)].append(s)

        return mapping.values()
    
solution = Solution()

print(solution.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"])) # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(solution.groupAnagrams(["x"])) # [["x"]]
print(solution.groupAnagrams([""])) # [""]