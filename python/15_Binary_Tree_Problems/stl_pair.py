import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    n_tok = cin()
    if n_tok is None:
        return
    n = int(n_tok)
    v = []
    for i in range(n):
        first = int(cin())
        second = int(cin())
        v.append((first, second))

    for i in range(n):
        print(f"{v[i][0]} {v[i][1]}")

if __name__ == "__main__":
    main()
