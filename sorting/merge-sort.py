def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) >> 1
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        k = 0
        while L and R:
            arr[k] = (R, L)[L[0] < R[0]].pop(0)
            k += 1
        arr[k:] = L + R


a = [7, 2, 5, 7, 1, 2, 3, 6, 9]
merge_sort(a)
print(a)
