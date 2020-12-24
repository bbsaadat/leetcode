class Solution:
    def validPalindrome(self, s: str) -> bool:

        
        s = list(s) 
        
        #start for
        for i in range(len(s)):
            #start if
            if s[i] != s[-(i+1)]:
                s1 = s[:]   
                s2 = s[:]
                s1.pop(i)
                s2.pop(-(i+1))  
                #start inner if
                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return True
                else:
                    return False
                #end inner if
            #end if
        else:
            return True
        #end for
