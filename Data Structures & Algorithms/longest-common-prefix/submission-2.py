class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                     return result
            result = result + strs[0][i]

        return result         
#Condtion - terminate loop as soon as character changed - but check all values at once. We don't have to do this for everystring.ALso if any string is shorter than also terminate the condiiton. Every single char compare with every single char of every single screen - o(n) = min(string)

    
        