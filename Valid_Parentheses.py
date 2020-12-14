class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        index = 0
        stack = []

        while(index != len(s) or len(stack) != 0):
            
            while index != len(s) and s[index] in "({[":
                stack.append(s[index])
                index += 1
                
            if index == len(s) or len(stack) == 0:
                return False
                
            if stack[-1] + s[index] not in ["()", "[]", "{}"]:
                return False
                break
            else:
                stack.pop()
                index += 1

        return(True)
