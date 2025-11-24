import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    n_token = cin()
    if n_token is None:
        return
    n = int(n_token)
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        a[i][i] = int(cin())

if __name__ == "__main__":
    main()
