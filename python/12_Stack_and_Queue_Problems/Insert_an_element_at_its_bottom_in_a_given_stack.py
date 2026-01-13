# Problem link: https://www.codingninjas.com/studio/problems/insert-an-element-at-its-bottom-in-a-given-stack_1171166

def pushAtBottom(st: list, x: int) -> list:
    new_st = []
    while len(st) > 0:
        new_st.append(st.pop())
    st.append(x)
    while len(new_st) > 0:
        st.append(new_st.pop())
    return st
