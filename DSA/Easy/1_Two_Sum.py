class Solution(object):
    # Time: O(n^2)
    # Space: O(1)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        for key,item in enumerate(nums):
            okey = target - item
            if okey in nums and nums.index(okey) != key:
                res.append(key)
                res.append(nums.index(okey))       
                return res     
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  
    print(s.twoSum([3, 2, 4], 6))        
    print(s.twoSum([3, 3], 6))           