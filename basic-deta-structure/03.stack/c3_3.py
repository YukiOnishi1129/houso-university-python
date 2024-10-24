import queue
# queueはFIFOキュー、優先順位付きキュー、LIFOキューを提供する
# LIFOキューはスタックとして使用できる
# Last In First Out
st = queue.LifoQueue(maxsize=64)
print("stack max size:", st.maxsize)
print("stack size:", st.qsize())

st.put(500)
st.put(200)
st.put(600)
print("stack size:", st.qsize())

print("push: 300")
st.put(300)
print("push: 100")
st.put(100)
print("stack size:", st.qsize())

print("pop:", st.get())
print("pop:", st.get())
print("stack size:", st.qsize())