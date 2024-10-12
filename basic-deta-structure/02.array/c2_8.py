# 線形探索の関数の例
# リストの先頭から順に比較し、探索キーを探す
# 最初に見つかったインデックスを返す
# 見つからなければNoneを返す
def linear_search(arr, key):
    """linear search"""
    arr_length = len(arr)
    for index in range(arr_length):
        if arr[index] == key:
            return index
    return None

