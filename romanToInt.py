class Solution:
    def romanToInt(self, s: str) -> int:

        D = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        S = [c for c in s]

        result = 0
        i = 0

        while (i < (len(S))):
            if i == len(S)-1:
                result = result + D[S[i]]
                break
            if D[S[i]] < D[S[i+1]]:
                result = result + (D[S[i+1]] - D[S[i]])
                i += 2
            else:
                result = result + D[S[i]]
                i +=1

        return(result)

