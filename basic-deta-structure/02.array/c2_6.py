import array

array_a = array.array('i', [10, 20, 30, 40])
array_b = array.array('i', [50, 60])
print(array_a)
print(array_b)

# ２個の配列を結合
array_c = array_a + array_b
print(array_c)