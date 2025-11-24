import sys

# Simulation of cin >>
_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    n_token = cin()
    if n_token is None:
        return
    n = int(n_token)
    q = int(cin())
    a = [0] * n
    for i in range(n):
        a[i] = int(cin())
    
    for i in range(q):
        x = int(cin())
        flag = 0
        for i in range(n):
            if a[i] == x:
                flag = 1
        if flag == 1:
            print("found")
        else:
            print("not found")

if __name__ == "__main__":
    main()
