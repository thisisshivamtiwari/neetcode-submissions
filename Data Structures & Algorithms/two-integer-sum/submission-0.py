class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution - if value of i + value of j = target. return [i,j] and i!=j
       #Hashmap can gives us what value is where instantly and we can do a target-index value = serach in hasmap and return 0.
       hashMap = {} 
       for i, n in enumerate(nums):
        diff = target-n
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[n] = i
       return   

      

    
        