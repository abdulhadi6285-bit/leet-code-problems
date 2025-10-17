def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    merged = sorted(nums1 + nums2)
    n = len(merged)

    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        mid1 = merged[n // 2 - 1]
        mid2 = merged[n // 2]
        return (mid1 + mid2) / 2


print("Problem #1 - Median of Two Sorted Arrays")
print("findMedianSortedArrays([1, 3], [2]) → 2.0")
print("findMedianSortedArrays([1, 2], [3, 4]) → 2.5")
print("findMedianSortedArrays([0, 0], [0, 0]) → 0.0")
print("findMedianSortedArrays([], [1]) → 1.0")
print("findMedianSortedArrays([2], []) → 2.0")
