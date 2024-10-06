list_a = [80, 40, 30, 20, 20]
print(list_a)

list_a.append(100)
print(list_a)

list_a.insert(2, 200)
print(list_a)

list_a.remove(200)
print(list_a)

item = list_a.pop(0)
print(list_a)
print(item)

# append (アペンド): 追加
# insert (インサート): 挿入
# remove (リムーブ): 削除
# pop (ポップ): 取り出し
## リスト中の指定された位置にある要素をリストから削除して、その要素を返す