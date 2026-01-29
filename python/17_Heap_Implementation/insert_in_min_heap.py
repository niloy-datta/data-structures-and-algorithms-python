import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def main():
    n_tok = cin()
    if n_tok is None:
        return
    n = int(n_tok)
    v = [0] * n
    for i in range(n):
        v[i] = int(cin())
    val = int(cin())
    v.append(val)
    cur_idx = len(v) - 1
    while cur_idx != 0:
        par_idx = (cur_idx - 1) // 2
        if v[par_idx] > v[cur_idx]:
            v[par_idx], v[cur_idx] = v[cur_idx], v[par_idx]
        else:
            break
        cur_idx = par_idx

    for x in v:
        print(x, end=" ")
    print()

if __name__ == "__main__":
    main()
