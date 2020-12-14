class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        given_num = x
        given_num_length = len(str(given_num))

        given_num = x
        reversed_num = 0


        for i in range(given_num_length):

            remainder = given_num % 10

            given_num = given_num - remainder 
            given_num = given_num//10

            reversed_num = reversed_num + remainder * 10**(given_num_length-(i+1))

        if x == reversed_num:
            return True
        else:
            return False
            
            












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


