class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, m, l, r):
            Left = arr[l : m + 1]
            Right = arr[m + 1 : r + 1]
            i = l
            j = 0
            k = 0

            while j < len(Left) and k < len(Right):
                if Left[j] < Right[k]:
                    arr[i] = Left[j]
                    j += 1
                else:
                    arr[i] = Right[k]
                    k += 1

                i += 1

            while j < len(Left):
                arr[i] = Left[j]
                j += 1
                i += 1

            while k < len(Right):
                arr[i] = Right[k]
                k += 1
                i += 1

        def mergesort(arr, l, r):
            if l >= r:
                return

            m = (l + r) // 2
            mergesort(arr, l, m)
            mergesort(arr, m + 1, r)
            merge(arr, m, l, r)

        mergesort(nums, 0, len(nums) - 1)
        return nums
