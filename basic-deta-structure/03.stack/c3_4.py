class MyStack:
    def __init__(self):
        self.data = []
        
    # リストのappend()メソッドを使ってデータを追加
    def push(self, data):
        self.data.append(data)
        
    # リストのpop()メソッドを使ってデータを取り出す
    def pop(self):
        return self.data.pop()
    
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