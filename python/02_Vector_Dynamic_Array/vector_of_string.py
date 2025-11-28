import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    n = int(lines[0])
    v = [""] * n
    for i in range(n):
        v[i] = lines[1 + i] if (1 + i) < len(lines) else ""
    for s in v:
        print(s)

if __name__ == "__main__":
    main()
