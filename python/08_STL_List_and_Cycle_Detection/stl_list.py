def main():
    # l = [1, 2, 3, 4, 5]
    # a = [10, 20, 30]
    v = [10, 20, 30]
    l2 = list(v)

    # l2.clear()
    # print(len(l2))
    while len(l2) < 5:
        l2.append(100)
    for val in l2:
        print(val)

if __name__ == "__main__":
    main()
