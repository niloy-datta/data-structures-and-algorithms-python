import sys

def main():
    s = sys.stdin.readline()
    if not s:
        return
    words = s.split()
    mp = {}
    for word in words:
        mp[word] = mp.get(word, 0) + 1

    for it_first in sorted(mp.keys()):
        print(f"{it_first} {mp[it_first]}")

if __name__ == "__main__":
    main()
