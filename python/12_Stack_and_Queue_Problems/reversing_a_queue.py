# Problem link: https://www.codingninjas.com/studio/problems/reversing-a-queue_982934

def reverseQueue(q):
    st = []
    while len(q) > 0:
        st.append(q.popleft())
    while len(st) > 0:
        q.append(st.pop())
    return q
