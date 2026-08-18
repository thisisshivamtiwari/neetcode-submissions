class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            # first approach = # o(n) operation 
            # # time = o(n^2)

            # second approach = sorting 
            # duplicates will be found in first  iteration
        
            #third approach is hashset  - we can directly check if value is contained by hasset or not.
            hasset = set()
            for n in nums:
                if n in hasset:
                    return True
                hasset.add(n)
            return False       
            