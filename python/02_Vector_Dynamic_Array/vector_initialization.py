def main():
    # v = []              # type 1
    # v = [0] * 10        # type 2
    # v = [-1] * 10       # type 3
    # v2 = list(v)        # type 4
    a = [1, 2, 3, 4, 5]
    # v = a[:5]           # type 5

    v = [1, 2, 3, 4]      # type 6
    for i in range(len(v)):
        print(v[i], end=" ")

if __name__ == "__main__":
    main()
