tuple_a = (80, 40, 30, 20, 20)
print(tuple_a)

tuple_b = 80, 40, 30, 20, 20
print(tuple_b)

print(tuple_a[2])

print(tuple_a[2:5])

print(30 in tuple_a)
print(90 in tuple_a)

i = len(tuple_a)
print(tuple_a)
print(i)

# tupleは要素を変更できない　イミュータブル
# tupleは順番を持ったコレクション型
# タブルの要素には、添え字[インデックス]を使ってアクセスできる
# コロンを使って表現されるスライスで、タプル要素を一部分取り出しできる
# 演算子 in を使った例で、タプル内に指定した要素が存在するか確かめることができる