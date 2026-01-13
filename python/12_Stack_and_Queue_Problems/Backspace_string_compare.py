# Problem link: https://leetcode.com/problems/backspace-string-compare/description/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st = []
        for c in s:
            if c == '#':
                if len(st) > 0:
                    st.pop()
            else:
                st.append(c)

        st2 = []
        for c in t:
            if c == '#':
                if len(st2) > 0:
                    st2.pop()
            else:
                st2.append(c)

        return st == st2
