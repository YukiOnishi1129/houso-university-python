class MyStack:
    def __init__(self):
        self.data = []
        
    # リストのappend()メソッドを使ってデータを追加
    def push(self, data):
        self.data.append(data)
        
    # リストのpop()メソッドを使ってデータを取り出す
    def pop(self):
        return self.data.pop()
    
    def is_empty(self):
        return not self.data
        # i.e.
        # return self.data == []
        
    def is_empty2(self):
        return len(self.data) == 0
    
    def is_empty3(self):
        return bool(not self.data)
    
    def display(self):
        print(self.data)
        
st = MyStack()

st.display()
st.push('H')
st.push('E')
st.push('L')
st.push('L')
st.push('O')
st.display()

print("pop:", st.pop())
print("pop:", st.pop())
print("pop:", st.pop())
print("pop:", st.pop())
print("pop:", st.pop())
st.display()