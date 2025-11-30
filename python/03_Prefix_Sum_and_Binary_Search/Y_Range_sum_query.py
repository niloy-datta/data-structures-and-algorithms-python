import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    n_token = cin()
    if n_token is None:
        return
    n = int(n_token)
    q = int(cin())
    v = [0] * (n + 1)
    for i in range(1, n + 1):
        v[i] = int(cin())

    pre = [0] * (n + 1)
    pre[1] = v[1]
    for i in range(2, n + 1):
        pre[i] = pre[i - 1] + v[i]

    while q > 0:
        q -= 1
        l = int(cin())
        r = int(cin())
        if l == 1:
            sum_val = pre[r]
        else:
            sum_val = pre[r] - pre[l - 1]
        print(sum_val)

if __name__ == "__main__":
    main()
