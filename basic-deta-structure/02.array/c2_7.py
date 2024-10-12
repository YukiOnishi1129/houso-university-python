import array

array_a = array.array('i', [10, 20, 30, 40])

print(array_a)

# append: 追加
# 末尾に要素を追加
print("append(50)")
array_a.append(50)
print(array_a)

# insert: 挿入
# indexの要素に値を挿入する
# 2番目に 20 を挿入
print("insert(2, 20)")
array_a.insert(2, 20)
print(array_a)

# remove: 削除
# 指定した要素を削除
print("remove(30)")
array_a.remove(30)
print(array_a)