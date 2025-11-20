import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    n_token = cin()
    if n_token is None:
        return
    n = int(n_token)

    i = n
    while i >= 1:
        print(i)
        i //= 3

if __name__ == "__main__":
    main()
