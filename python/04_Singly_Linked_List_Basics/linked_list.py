def main():
    v = [1, 2, 3, 4, 5]
    v.append(100)
    print(f"{id(v[4])} {id(v[5])}")

if __name__ == "__main__":
    main()
