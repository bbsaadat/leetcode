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
            


