def merge_sort(arr):

    if len(arr) > 1 :
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R) :

            if L[i] < R[j] :
                arr[k] = L[i]
                k += 1
                i += 1

            else :
                arr[k] = R[j]
                k += 1
                j += 1

        if i < len(L):

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
        if j < len(R) :
            arr[k] = R[j]
            j += 1
            k += 1
