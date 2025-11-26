def main():
    v = []
    v.append(10)
    v.append(20)
    v.append(30)
    while len(v) < 7:
        v.append(100)

    for i in range(len(v)):
        print(v[i], end=" ")

if __name__ == "__main__":
    main()
