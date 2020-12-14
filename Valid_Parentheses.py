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

            
            












# s = "()[]{}"
# if len(s) % 2 != 0:
#     print (False)

# L_left = [] 
# L_right = []

# pointer = 0

# while(pointer != len(s)):
#     if s[pointer] in "({[":
#         L_left.append( s[pointer] )
#         pointer += 1
#     elif (pointer < len(s)):
#         if s[pointer] in "]})":
#             L_right.append( s[pointer] )
#             pointer += 1
#     else:
#         break


# if len(L_left) != len(L_right):
#     print(False)

# print(L_left, L_right)
# for i in range(len(L_left)):
#     if L_left[i] + L_right[-(i+1)] not in ["()", "{}", "[]"] and L_left[i] + L_right[i] not in ["()", "{}", "[]"]:
#         print(False)
    
    
# print(True)


