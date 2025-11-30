import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    n_token = cin()
    if n_token is None:
        return
    n = int(n_token)
    a = [0] * n
    for i in range(n):
        a[i] = int(cin())
    val = int(cin())
    flag = 0

    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == val:
            flag = 1
            break
        elif a[mid] > val:
            r = mid - 1
        else:
            l = mid + 1

    if flag == 1:
        print("Found")
    else:
        print("Not found")

if __name__ == "__main__":
    main()
