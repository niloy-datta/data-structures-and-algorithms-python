import sys

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

def insert_heap(v, val):
    v.append(val)
    cur_idx = len(v) - 1
    while cur_idx != 0:
        par_idx = (cur_idx - 1) // 2
        if v[par_idx] > v[cur_idx]:
            v[par_idx], v[cur_idx] = v[cur_idx], v[par_idx]
        else:
            break
        cur_idx = par_idx

def print_heap(v):
    for x in v:
        print(x, end=" ")
    print()

def delete_heap(v):
    print(f"{v[0]} Deleted. -> ", end="")
    v[0] = v[-1]
    v.pop()
    if len(v) == 0:
        return
    cur_idx = 0
    while True:
        left_idx = cur_idx * 2 + 1
        right_idx = cur_idx * 2 + 2

        left_val = float('inf')
        right_val = float('inf')
        if left_idx < len(v):
            left_val = v[left_idx]
        if right_idx < len(v):
            right_val = v[right_idx]

        if left_val <= right_val and left_val < v[cur_idx]:
            v[left_idx], v[cur_idx] = v[cur_idx], v[left_idx]
            cur_idx = left_idx
        elif right_val < left_val and right_val < v[cur_idx]:
            v[right_idx], v[cur_idx] = v[cur_idx], v[right_idx]
            cur_idx = right_idx
        else:
            break

def main():
    v = []
    n_tok = cin()
    if n_tok is None:
        return
    n = int(n_tok)
    for i in range(n):
        val = int(cin())
        insert_heap(v, val)

    print_heap(v)
    delete_heap(v)
    print_heap(v)
    delete_heap(v)
    print_heap(v)
    delete_heap(v)
    print_heap(v)
    delete_heap(v)
    print_heap(v)
    delete_heap(v)
    print_heap(v)

if __name__ == "__main__":
    main()
