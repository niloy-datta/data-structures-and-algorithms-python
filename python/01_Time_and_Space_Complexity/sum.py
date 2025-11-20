import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    n_token = cin()
    if n_token is None:
        return
    n = int(n_token)
    sum_val = 0

    # using loop
    # for i in range(1, n + 1):
    #     sum_val += i

    # using formula
    # sum_val = (n * (n + 1)) // 2

    print(sum_val)

if __name__ == "__main__":
    main()
