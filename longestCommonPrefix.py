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
            


