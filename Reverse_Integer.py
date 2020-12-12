class Solution:
    def reverse(self, x: int) -> int:

        
        sign = 1
        
        y = str(x)
        if "-" in y:
            sign = -1
            y = y[1:]
            
        y = y[::-1]
        y = sign*int(y)
        if y > int(2**31) or y < (-1*int(2**31)-1):
            return 0
        return (y)
            