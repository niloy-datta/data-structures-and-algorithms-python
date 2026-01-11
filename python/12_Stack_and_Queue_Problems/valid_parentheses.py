# Problem link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
            else:
                if len(st) == 0:
                    return False
                else:
                    if c == ')' and st[-1] == '(':
                        st.pop()
                    elif c == '}' and st[-1] == '{':
                        st.pop()
                    elif c == ']' and st[-1] == '[':
                        st.pop()
                    else:
                        return False
        if len(st) == 0:
            return True
        else:
            return False
