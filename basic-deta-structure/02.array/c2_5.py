import array

array_a = array.array('i', [10, 20, 30, 40])
print(array_a)
print("array_a[2 = 300]")
array_a[2] = 300
print(array_a)

print("del array_a[1]")
# del: index 1 の要素を削除
del array_a[1]
print(array_a)

print("10 in array_a")
# in: 10 が array_a に含まれているかどうか
print(10 in array_a)
print("50 in array_a")
# in: 50 が array_a に含まれているかどうか
print(50 in array_a)