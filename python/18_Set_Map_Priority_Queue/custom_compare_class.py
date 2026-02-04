import sys
import heapq

_tokens = iter(sys.stdin.read().split())
def cin():
    return next(_tokens, None)

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

class cmp:
    def __init__(self, obj):
        self.obj = obj

    def __lt__(self, other):
        # class cmp operator()(Student l, Student r)
        # if l.marks > r.marks return true
        # else if l.marks < r.marks return false
        # else return l.roll > r.roll
        l = self.obj
        r = other.obj
        if l.marks > r.marks:
            return True
        elif l.marks < r.marks:
            return False
        else:
            return l.roll > r.roll

def main():
    pq = []
    n_tok = cin()
    if n_tok is None:
        return
    n = int(n_tok)
    for i in range(n):
        name = cin()
        roll = int(cin())
        marks = int(cin())
        obj = Student(name, roll, marks)
        heapq.heappush(pq, cmp(obj))

    while len(pq) > 0:
        top_student = heapq.heappop(pq).obj
        print(f"{top_student.name} {top_student.roll} {top_student.marks}")

if __name__ == "__main__":
    main()
