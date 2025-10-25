class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res=nums1+nums2
        res.sort()
        size=len(res)
        if (size % 2 == 0):
            median = (res[size // 2 - 1] + res[size // 2]) / 2.0
        else:
            median = res[size // 2]
        return median
    
if __name__=="__main__":
    sol=Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    sol.findMedianSortedArrays(nums1,nums2)