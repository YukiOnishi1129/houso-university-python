# 二分探索のコード例
# あらかじめ配列の要素が昇順に並んでいることが前提
def binary_search(arr, key):
    """binary search"""
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = low + (low + high) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            high = mid - 1
        else:
           low = mid + 1
    return None
