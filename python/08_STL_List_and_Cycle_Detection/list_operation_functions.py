def main():
    l = [20, 30, 10, 50, 30, 60, 60, 10]
    # l.sort()
    # l.sort(reverse=True)

    # l = list(dict.fromkeys(l))
    l.reverse()
    for val in l:
        print(val)

if __name__ == "__main__":
    main()
