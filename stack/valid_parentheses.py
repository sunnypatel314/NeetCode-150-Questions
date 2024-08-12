class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {")": "(", "]": "[", "}": "{"}

        stack = ["$"]

        for c in s:
            if c not in mapping:
                stack.append(c)
                continue
            if mapping.get(c) == stack[-1]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 1
            
            
solution = Solution()

print(solution.isValid(s = "[]")) # True
print(solution.isValid(s = "([{}])")) # True
print(solution.isValid(s = "[(])")) # False
