import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    st = []
    n_tok = cin()
    if n_tok is None:
        return
    n = int(n_tok)
    for i in range(n):
        val = int(cin())
        st.append(val)

    while len(st) > 0:
        print(st[-1])
        st.pop()

if __name__ == "__main__":
    main()
