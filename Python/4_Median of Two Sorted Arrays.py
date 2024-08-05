class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total_len = m+n
        if total_len == 0:
            return 0
        final_arr = []
        cont_m = cont_n = 0
        while(cont_m < m or cont_n < n):
            if (cont_m >= m):
                final_arr = final_arr + nums2[cont_n:n]
                break
            elif (cont_n >= n):
                final_arr = final_arr + nums1[cont_m:m]
                break
            elif nums1[cont_m] <= nums2[cont_n]:
                final_arr.append(nums1[cont_m])
                cont_m += 1
            elif nums2[cont_n] <= nums1[cont_m]:
                final_arr.append(nums2[cont_n])
                cont_n += 1
        print(final_arr)
        if (total_len) % 2 == 0:
            median = (final_arr[int(total_len/2)] + final_arr[int((total_len/2)-1)])/2
            return median
        return final_arr[total_len//2]