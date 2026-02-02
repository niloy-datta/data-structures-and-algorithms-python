import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    s = set()
    n_tok = cin()
    if n_tok is None:
        return
    n = int(n_tok)
    while n > 0:
        n -= 1
        val = int(cin())
        s.add(val)     # logN

    for it in sorted(s):
        print(it)

    if 40 in s:             # logN
        print("Ache")
    else:
        print("Nai")

if __name__ == "__main__":
    main()
