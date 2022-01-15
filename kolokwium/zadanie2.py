def bubble_sort(arr):
    n = len(arr)
    j = 0   # z n-2 na 0
    while j <= n - 2:   # z 0 na n-2 oraz z >= na <=
        i = 0
        while i <= j:
            if arr[i] < arr[i + 1]:   # z > na < żeby sortowało nierosnąco (malejąco)
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
        j += 1  # z -= na +=
    return arr


print(bubble_sort([15, -5, 10, 27, -12, 3, 9, 11]))
