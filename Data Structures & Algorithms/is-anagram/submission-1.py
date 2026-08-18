class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Condition - length and character should be same for both string.
        # Brute force -> HashMap<s,t> = char and value key and count can be matched   
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)    

        #By using two hash maps (or dictionaries), we track the frequency of every character in each string.
        # if len(s) != len(t):
        #  return False
        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # return countS == countT 


        #Solution 3
        return Counter(s)==Counter(t)

       
       