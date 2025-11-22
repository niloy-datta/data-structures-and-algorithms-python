import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    n_token = cin()
    if n_token is None:
        return
    n = int(n_token)

    i = 1
    while i * i <= n:
        if n % i == 0:
            print(f"{i} {n // i}", end=" ")
        i += 1

if __name__ == "__main__":
    main()
