import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    n_token = cin()
    if n_token is None:
        return
    n = int(n_token)

    for i in range(1, n + 1, 2):
        print(i, end=" ")
    print()
    for i in range(1, n + 1):
        print(i, end=" ")

if __name__ == "__main__":
    main()
