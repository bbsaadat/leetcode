class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if strs == [] or strs == [""]:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        prefix_List = (len(strs)-1)*[""]
        min_str_size = len(strs[0])
        for word in strs:
            if len(word) < min_str_size:
                min_str_size = len(word)



        for list_index,(a,b) in enumerate(zip(strs, strs[1:])):
            print(a,b)
            for char_index in range(min_str_size):
                if(a[char_index] == b[char_index]):
                    prefix_List[list_index] += a[char_index]
                else:
                    break

        return min(prefix_List, key=len)
            












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


