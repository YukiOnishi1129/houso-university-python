import collections

# deque: 先頭と末尾の要素に対して高速に操作ができる
st = collections.deque()
print("stack:", st)

st.append(500)
st.append(200)
st.append(600)
print("stack:", st)

print("push: 300")
st.append(300)
print("push: 100")
st.append(100)
print("stack:", st)

print("pop:", st.pop())
print("pop:", st.pop())
print("stack:", st)