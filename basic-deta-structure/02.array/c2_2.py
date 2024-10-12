import array
# arrayはimportしないと使えない

# 型コードを用いて型を指定
# i: integer(整数)
array_a = array.array('i', [1, 2, 3, 4, 5])

for i in array_a:
    print(i, end = " ")