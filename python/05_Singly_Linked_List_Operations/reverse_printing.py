def rec(i, n):
    # base case
    if i > n:
        return
    rec(i + 1, n)
    print(i)

def main():
    n = 5
    rec(1, n)

if __name__ == "__main__":
    main()
