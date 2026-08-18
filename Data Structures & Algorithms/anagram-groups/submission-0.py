class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #first find anagram by hashmap and then save it to. By mapping char count to list of anagrams. 
        hashmap = defaultdict(list)
        for s in strs:
            count = [0] * 26 #a-z
            for c in s:
                count[ord(c) - ord("a")] += 1
                #a= 65 -> 0, 65-65
                #b= 66 -> 1, 66-65
            hashmap[tuple(count)].append(s)   
            #count is list and list cannot be keys so changed it to tuple
        return list(hashmap.values())   