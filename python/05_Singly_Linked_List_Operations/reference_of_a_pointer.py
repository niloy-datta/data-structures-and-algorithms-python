def fun(p):
    p[0] = None

def main():
    x = 10
    p = [x]
    fun(p)
    print("In Main:", p[0])

if __name__ == "__main__":
    main()
